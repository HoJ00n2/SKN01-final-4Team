<template>
    <div class="mbti-container" ref="container">
        <h1 class="main-title" ref="mainTitle">{{ mainTitle }}</h1>
        <h1 class="mbti-title" ref="title">{{ mbtiType }}</h1>
        <div class="content">
            <div class="strengths">
                <h2 class="section-title" ref="strengthsTitle">장점</h2>
                <div v-for="(strength, index) in strengths" :key="strength.title" class="strength"
                    :ref="`strength${index}`">
                    <span class="emoji">{{ strength.emoji }}</span>
                    <div>
                        <h3>{{ strength.title }}</h3>
                        <p>{{ strength.description }}</p>
                    </div>
                </div>
            </div>
            <div class="weaknesses">
                <h2 class="section-title" ref="weaknessesTitle">단점</h2>
                <div v-for="(weakness, index) in weaknesses" :key="weakness.title" class="weakness"
                    :ref="`weakness${index}`">
                    <span class="emoji">{{ weakness.emoji }}</span>
                    <div>
                        <h3>{{ weakness.title }}</h3>
                        <p>{{ weakness.description }}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer" ref="footer">
            <p>{{ strategyText }}</p>
        </div>
    </div>
</template>

<script>
import anime from 'animejs/lib/anime.es.js';

export default {
    name: 'MBTIPersonality',
    props: {
        strengths: {
            type: Array,
            required: true
        },
        weaknesses: {
            type: Array,
            required: true
        },
        mbtiType: {
            type: String,
            required: true
        },
        strategyText: {
            type: String,
            required: true
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
                duration: 500
            });

            timeline.add({
                targets: this.$refs.title,
                opacity: [0, 1],
                translateY: ['-30px', '0px'],
                duration: 1000
            });

            timeline.add({
                targets: this.$refs.strengthsTitle,
                opacity: [0, 1],
                translateY: ['-20px', '0px'],
                duration: 800
            }, '-=500');

            this.strengths.forEach((_, index) => {
                timeline.add({
                    targets: this.$refs[`strength${index}`],
                    opacity: [0, 1],
                    translateX: ['-30px', '0px'],
                    duration: 600
                }, '-=400');
            });

            timeline.add({
                targets: this.$refs.weaknessesTitle,
                opacity: [0, 1],
                translateY: ['-20px', '0px'],
                duration: 800
            }, '+=200');

            this.weaknesses.forEach((_, index) => {
                timeline.add({
                    targets: this.$refs[`weakness${index}`],
                    opacity: [0, 1],
                    translateX: ['30px', '0px'],
                    duration: 600
                }, '-=400');
            });

            timeline.add({
                targets: this.$refs.footer,
                opacity: [0, 1],
                translateY: ['20px', '0px'],
                duration: 800
            }, '+=200');
        }
    }
}
</script>

<style scoped>
.mbti-container {
    max-width: 800px;
    padding: 20px;
    margin: 0 auto;
    margin-top: 20px;
    margin-bottom: 50px;
}

.main-title {
    text-align: center;
    font-size: 2em;
    margin-bottom: 30px;
}

.mbti-title {
    text-align: center;
    font-size: 2.5em;
    margin-bottom: 30px;
}

.content {
    display: flex;
    justify-content: space-between;
}

.strengths,
.weaknesses {
    width: 48%;
}

.section-title {
    font-size: 1.5em;
    border-bottom: 2px solid #333;
    padding-bottom: 20px;
    margin-bottom: 20px;
}

.strength,
.weakness {
    display: flex;
    align-items: flex-start;
    margin-top: 20px;
    margin-bottom: 20px;
}

.emoji {
    font-size: 2em;
    margin-right: 10px;
}

h3 {
    margin: 0 0 5px 0;
}

p {
    margin: 0;
    font-size: 0.9em;
}

.footer {
    margin-top: 20px;
    font-style: italic;
    text-align: center;
    font-size: 14px;
    opacity: 0;
}
</style>