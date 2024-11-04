<template>
    <div class="background">
        <div class="loading-container">
            <div class="chaotic-orbit"></div>
            <p class="loading-text">분석 결과를 불러오고 있어요.<br>잠시만 기다려주세요.</p>
        </div>
    </div>
</template>

<script>
export default {
    setup() {
        return {}
    }
}
</script>

<style>
.background {
    width: 100%;
    height: 100vh;
    background-color: black;
    display: flex;
    justify-content: center;
    align-items: center;
}

.loading-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.chaotic-orbit {
    --uib-size: 25px;
    --uib-speed: 1.5s;
    --uib-color: rgb(255, 255, 255);
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    height: var(--uib-size);
    width: var(--uib-size);
    animation: rotate936 calc(var(--uib-speed) * 1.667) infinite linear;
}

.chaotic-orbit::before,
.chaotic-orbit::after {
    content: '';
    position: absolute;
    height: 60%;
    width: 60%;
    border-radius: 50%;
    background-color: var(--uib-color);
    will-change: transform;
    flex-shrink: 0;
}

.chaotic-orbit::before {
    animation: orbit var(--uib-speed) linear infinite;
}

.chaotic-orbit::after {
    animation: orbit var(--uib-speed) linear calc(var(--uib-speed) / -2) infinite;
}

.loading-text {
    color: white;
    margin-top: 20px;
    font-size: 16px;
    text-align: center;
    opacity: 50%;
}

@keyframes rotate936 {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes orbit {
    0% {
        transform: translate(calc(var(--uib-size) * 0.5)) scale(0.73684);
        opacity: 0.65;
    }
    50% {
        transform: translate(calc(var(--uib-size) * -0.5)) scale(0.73684);
        opacity: 0.65;
    }
    100% {
        transform: translate(calc(var(--uib-size) * 0.5)) scale(0.73684);
        opacity: 0.65;
    }
}
</style>