<template>
  <div class="about-page">
    <h1 class="about-title">총정리</h1>
    <div class="image-container">
      <img :src="require(`@/assets/images/fixed/FinalSummaryContent/남자.webp`)" alt="Summary Image"
        class="centered-image">
    </div>
    <div class="content" ref="content">
      <div v-for="(card, index) in cards" :key="index" class="card-container" :ref="`cardContainer-${index}`"
        @mouseenter="onMouseEnter($event, index)" @mouseleave="onMouseLeave($event, index)">
        <div class="card" :ref="`card-${index}`">
          <div class="card-content">
            <h3>{{ card.title }}</h3>
            <p class="period">{{ card.period }}</p>
            <p class="description">{{ card.content }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import anime from 'animejs/lib/anime.es.js';

export default {
  name: 'AboutPage',
  data() {
    return {
      cards: [
        { title: '콘텐츠 제작 및 업로드', period: '지속적', content: '정기적으로 콘텐츠를 제작하여 팬들의 기대감을 유지하세요' },
        { title: '아이디어 발굴', period: '1-2개월', content: '독특한 캐릭터나 스타일을 찾아내고, 운동 콘텐츠 아이디어를 구상하세요.' },
        { title: '팬과의 소통 강화', period: '지속적', content: '댓글과 메시지에 적극적으로 응답하며 팬들과의 유대감을 형성하세요.' },
        { title: '협업 및 네트워킹', period: '2-6개월', content: '다른 인플루언서와의 협업을 통해 새로운 팬층을 확보하세요.' },
        { title: '목소리 활용 극대화', period: '주 2-3번', content: '목소리를 활용한 콘텐츠를 통해 팬들과의 소통을 극대화하세요.' }
      ],
      observer: null,
      animationInProgress: false
    };
  },
  mounted() {
    this.setupIntersectionObserver();
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
        if (entries[0].isIntersecting && !this.animationInProgress) {
          this.animateCards();
        }
      }, options);

      this.observer.observe(this.$refs.content);
    },
    animateCards() {
      this.animationInProgress = true;
      const timeline = anime.timeline({
        easing: 'easeOutQuad',
        duration: 250,
        complete: () => {
          this.animationInProgress = false;
        }
      });

      this.cards.forEach((_, index) => {
        timeline.add({
          targets: this.$refs[`card-${index}`][0],
          translateY: [50, 0],
          opacity: [0, 1],
          delay: index * 100
        });
      });
    },
    resetCards() {
      this.cards.forEach((_, index) => {
        const card = this.$refs[`card-${index}`][0];
        card.style.transform = 'translateY(100px)';
        card.style.opacity = '0';
      });
    },
    onMouseEnter(event, index) {
      anime({
        targets: this.$refs[`card-${index}`][0],
        scale: 1.1,
        translateY: -10,
        boxShadow: '0 15px 30px rgba(0, 0, 0, 0.2)',
        duration: 150,
        easing: 'easeOutQuad'
      });
    },
    onMouseLeave(event, index) {
      anime({
        targets: this.$refs[`card-${index}`][0],
        scale: 1,
        translateY: 0,
        boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
        duration: 300,
        easing: 'easeOutQuad'
      });
    }
  }
}
</script>

<style scoped>
.about-page {
  font-family: Arial, sans-serif;
  max-width: 1200px;
  margin: 10% auto 5%;
  padding: 20px;
}

.about-title {
  color: #000;
  text-align: center;
  font-size: 2.5em;
  margin-bottom: 30px;
}

.image-container {
  text-align: center;
  margin-bottom: 30px;
}

.centered-image {
  max-width: 20%;
  border-radius: 50%;
  height: auto;
}

.content {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 20px;
}

.card-container {
  width: calc(20% - 16px);
  aspect-ratio: 1;
}

.card {
  background-color: white;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.3s ease;
}

.card-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

h3 {
  color: #34495e;
  font-size: 1em;
  text-align: center;
  margin-bottom: 5px;
}

.period {
  color: #666;
  font-size: 0.8em;
  text-align: center;
  margin-bottom: 10px;
}

.description {
  color: #666;
  line-height: 1.3;
  font-size: 0.9em;
  text-align: center;
  flex-grow: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (max-width: 1200px) {
  .card-container {
    width: calc(33.33% - 13.33px);
  }
}

@media (max-width: 768px) {
  .card-container {
    width: calc(50% - 10px);
  }

  .centered-image {
    max-width: 70%;
  }
}

@media (max-width: 480px) {
  .card-container {
    width: 100%;
  }

  .centered-image {
    max-width: 90%;
  }
}
</style>