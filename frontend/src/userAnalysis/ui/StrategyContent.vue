<template>
  <div class="strategy-container" ref="container">
    <h1 class="main-title" ref="mainTitle">콘텐츠 전략</h1>
    <p class="subtitle" ref="subtitle">{{ subtitle }}</p>
    <div class="content">
      <div v-for="(strategy, index) in strategies" :key="strategy.title" class="strategy-item"
        :ref="el => { if (el) strategyRefs[index] = el }">
        <span class="emoji">{{ strategy.emoji }}</span>
        <div class="strategy-text">
          <h3>{{ strategy.title }}</h3>
          <p>{{ strategy.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import anime from 'animejs/lib/anime.es.js';

export default {
  name: 'StrategyContent',
  props: {
    strategies: {
      type: Array,
      required: true
    },
    subtitle: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      strategyRefs: []
    }
  },
  mounted() {
    this.setupIntersectionObserver()
  },
  beforeUnmount() {
    if (this.observer) {
      this.observer.disconnect()
    }
  },
  methods: {
    setupIntersectionObserver() {
      this.observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            this.animateContent()
            this.observer.disconnect()
          }
        })
      }, { threshold: 0.1 })
      this.observer.observe(this.$refs.container)
    },
    animateContent() {
      const timeline = anime.timeline({
        easing: 'easeOutExpo'
      });

      timeline.add({
        targets: this.$refs.mainTitle,
        opacity: [0, 1],
        translateY: ['-30px', '0px'],
        duration: 800
      }).add({
        targets: this.$refs.subtitle,
        opacity: [0, 1],
        translateY: ['-20px', '0px'],
        duration: 800
      }, '-=400');

      this.strategyRefs.forEach((el, index) => {
        timeline.add({
          targets: el,
          opacity: [0, 1],
          translateX: ['-30px', '0px'],
          duration: 600
        }, '-=400');
      });
    }
  }
}
</script>

<style scoped>
.strategy-container {
  background-color: #1a1a1a;
  padding: 40px;
  max-width: 800px;
  margin: 0 auto;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.main-title {
  text-align: center;
  font-size: 2.5em;
  margin-bottom: 20px;
  color: #ffffff;
}

.subtitle {
  text-align: center;
  font-size: 1.2em;
  margin-bottom: 40px;
  color: #cccccc;
}

.content {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.strategy-item {
  display: flex;
  align-items: flex-start;
  background-color: #2a2a2a;
  padding: 20px;
  border-radius: 8px;
  transition: transform 0.3s ease;
}

.strategy-item:hover {
  transform: translateY(-5px);
}

.emoji {
  font-size: 2.5em;
  margin-right: 20px;
  min-width: 50px;
  text-align: center;
}

.strategy-text {
  flex: 1;
}

h3 {
  margin: 0 0 10px 0;
  color: #ffffff;
  font-size: 1.3em;
}

p {
  margin: 0;
  color: #cccccc;
  font-size: 1em;
  line-height: 1.5;
}
</style>