<template>
  <div class="third-content">
    <div class="content-wrapper">
      <h2 class="subtitle">Key Point # 2</h2>
      <h1 class="title">
        <template v-for="(word, index) in words1" :key="'word1-'+index">
          <span :ref="'word1-'+index" class="gradient-word">{{ word }}</span>
          <span v-if="index < words1.length - 1">&nbsp;</span>
        </template>
        <br>
        <template v-for="(word, index) in words2" :key="'word2-'+index">
          <span :ref="'word2-'+index" class="gradient-word">{{ word }}</span>
          <span v-if="index < words2.length - 1">&nbsp;</span>
        </template>
      </h1>
      <div class="features">
        <div class="feature-list">
          <div class="feature-item">
            <h4>콘텐츠 카테고리</h4>
            <p>운동, 뷰티, 음악, 여행, 게임, 요리 등<br>다양한 콘텐츠 카테고리를 제공해요.</p>
          </div>
          <div class="feature-item">
            <h4>활동 플랫폼</h4>
            <p>유튜브, 틱톡, 인스타그램 등<br>사용자에게 적합한 플랫폼을 추천해요.</p>
          </div>
          <div class="feature-item">
            <h4>롤모델</h4>
            <p>타 인플루언서들의 활동을 보고<br>자신만의 롤모델을 찾아볼 수 있어요.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ThirdContent',
  data() {
    return {
      observer: null,
      words1: '사용자에게 어울리는 콘텐츠 카테고리,'.split(' '),
      words2: '활동 플랫폼, 롤모델을 찾아드려요.'.split(' '),
      animationDuration: 100,
      delayBetweenWords: 100
    }
  },
  mounted() {
    this.setupIntersectionObserver();
    this.updateAnimationDuration();
  },
  beforeUnmount() {
    if (this.observer) {
      this.observer.disconnect();
    }
  },
  methods: {
    setupIntersectionObserver() {
      const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
      };

      this.observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            this.animateGradientText();
          } else {
            this.resetGradientText();
          }
        });
      }, options);

      this.observer.observe(this.$el);
    },
    updateAnimationDuration() {
      document.documentElement.style.setProperty('--animation-duration', `${this.animationDuration}ms`);
    },
    animateGradientText() {
      const animateWord = (word, delay) => {
        setTimeout(() => {
          word.classList.remove('animate', 'final-color');
          void word.offsetWidth;
          word.classList.add('animate');
          setTimeout(() => {
            word.classList.add('final-color');
          }, this.animationDuration);
        }, delay);
      };

      const words1 = this.words1.map((_, i) => this.$refs[`word1-${i}`][0]);
      const words2 = this.words2.map((_, i) => this.$refs[`word2-${i}`][0]);

      words1.forEach((word, index) => {
        animateWord(word, index * this.delayBetweenWords);
      });

      const line1Duration = words1.length * this.delayBetweenWords;

      words2.forEach((word, index) => {
        animateWord(word, line1Duration + index * this.delayBetweenWords);
      });
    },
    resetGradientText() {
      [...this.words1, ...this.words2].forEach((_, i) => {
        const word1 = this.$refs[`word1-${i}`];
        const word2 = this.$refs[`word2-${i}`];
        if (word1) word1[0].classList.remove('animate', 'final-color');
        if (word2) word2[0].classList.remove('animate', 'final-color');
      });
    }
  }
}
</script>

<style scoped>
.third-content {
  background-color: #f5f5f5;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 80px 0;
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  width: 100%;
}

.subtitle {
  font-size: 32px;
  color: #333;
  margin-bottom: 20px;
}

.title {
  font-size: 48px;
  font-weight: bold;
  color: #000;
  margin-bottom: 40px;
  line-height: 1.2;
}

.gradient-word {
  background: linear-gradient(to right, rgba(211,122,47,1) 0%, rgba(211,122,47,1) 50%, rgba(0,0,0,1) 100%);
  background-size: 200% 100%;
  background-position: 100% 0;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
  display: inline-block;
  transition: all 0.1s ease;
  opacity: 0.1;
}

.gradient-word.animate {
  animation: fillLeftToRight var(--animation-duration) forwards;
  opacity: 1;
}

.gradient-word.final-color {
  background: none;
  -webkit-text-fill-color: #000000;
  color: #000000;
}

@keyframes fillLeftToRight {
  0% {
    background-position: 100% 0;
  }
  100% {
    background-position: 0 0;
  }
}

.features {
  display: flex;
  justify-content: space-between;
}

.feature-list {
  flex: 0 0 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.feature-item {
  flex: 0 0 33%;
  margin-bottom: 30px;
}

.feature-item h4 {
  font-size: 20px;
  margin-bottom: 10px;
}

.feature-item p {
  font-size: 16px;
  color: #666;
}

@media (max-height: 800px) {
  .third-content {
    height: auto;
    min-height: 100vh;
    padding: 80px 0;
  }
}
</style>