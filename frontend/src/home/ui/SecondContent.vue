<template>
  <div class="second-content">
    <div class="content-wrapper">
      <h2 class="subtitle">Key Point # 1</h2>
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
    </div>
  </div>
</template>

<script>
export default {
  name: 'SecondContent',
  data() {
    return {
      observer: null,
      words1: '사용자 개인 성향 조사 데이터 분석을 통해'.split(' '),
      words2: '인플루언서로 성장할 최적의 솔루션을 제공해요.'.split(' '),
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
.second-content {
  background-color: #000000;
  min-height: 100vh;
  display: flex;
  align-items: center;
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  width: 100%;
}

.subtitle {
  font-size: 32px;
  color: #ffffff;
  margin-bottom: 20px;
  text-align: center;
}

.title {
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 40px;
  line-height: 1.2;
  text-align: center;
}

.gradient-word {
  background: linear-gradient(to right, rgba(211,122,47,1) 0%, rgba(211,122,47,1) 50%, rgba(255,255,255,1) 100%);
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
  -webkit-text-fill-color: #ffffff;
  color: #ffffff;
}

@keyframes fillLeftToRight {
  0% {
    background-position: 100% 0;
  }
  100% {
    background-position: 0 0;
  }
}
</style>