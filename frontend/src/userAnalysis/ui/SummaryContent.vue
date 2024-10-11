<template>
  <div class="summary-content" ref="container">
    <div class="content-wrapper">
      <h2 class="main-title" ref="mainTitle">
        {{ title }}<br><br>
      </h2>
      <h1 class="summary" ref="summary">
        {{ summary }}
      </h1>
    </div>
  </div>
</template>

<script>
import anime from 'animejs/lib/anime.es.js';

export default {
  name: 'SummaryContent',
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      observer: null,
      title: '1. 입력 요약',
      summary: this.data,
    }
  },
  mounted() {
    console.log("SummaryContent 출력",this.data);
    this.setupIntersectionObserver();
  },
  beforeUnmount() {
    if (this.observer) {
      this.observer.disconnect();
    }
  },
  methods: {
    setupIntersectionObserver() {
      this.observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            this.animateContent();
            this.observer.disconnect();
          }
        });
      }, { threshold: 0.1 });

      this.observer.observe(this.$refs.container);
    },
    animateContent() {
      anime.timeline({
        easing: 'easeOutExpo',
      })
      .add({
        targets: this.$refs.mainTitle,
        opacity: [0, 1],
        translateY: ['-30px', '0px'],
        duration: 500,
      })
      .add({
        targets: this.$refs.summary,
        opacity: [0, 1],
        translateY: ['-20px', '0px'],
        duration: 1000,
        delay: 0
      });
    },
  }
}
</script>

<style scoped>
.summary-content {
  background-color: #000000;
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

.main-title {
  font-size: 32px;
  color: #ffffff;
  margin-bottom: 20px;
  text-align: center;
  opacity: 0; /* 초기에 투명하게 설정 */
}

.summary {
  font-size: 34px;
  font-weight: regular;
  color: #ffffff;
  margin-bottom: 40px;
  line-height: 1.2;
  text-align: center;
  opacity: 0; /* 초기에 투명하게 설정 */
}

@media (max-height: 800px) {
  .summary-content {
    height: auto;
    min-height: 100vh;
    padding: 80px 0;
  }
}
</style>
