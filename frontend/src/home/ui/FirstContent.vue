<template>
  <div class="main-container">
    <!-- <div class="video-container">
      <video ref="videoPlayer" class="fullscreen-video" :src="videoSource" autoplay muted playsinline
        @play="startOverlayTimer" @error="handleError"></video>
      <transition name="fade"> -->
    <div class="background-container">
      <transition name="fade">
        <div class="overlay">
          <div class="overlay-text">
            <h1 :class="{ 'fade-in': showTitle }">{{ overlayTitleOne }}</h1>
            <h1 :class="{ 'fade-in': showTitle }">{{ overlayTitleTwo }}</h1>
            <p :class="{ 'fade-in': showDescription }">{{ overlayDescription }}</p>
          </div>
          <button class="button mt-10" :class="{ 'fade-in': showButton }">
            <div class="dots_border"></div>
            <path class="path" stroke-linejoin="round" stroke-linecap="round" stroke="black" fill="black"
              d="M14.187 8.096L15 5.25L15.813 8.096C16.0231 8.83114 16.4171 9.50062 16.9577 10.0413C17.4984 10.5819 18.1679 10.9759 18.903 11.186L21.75 12L18.904 12.813C18.1689 13.0231 17.4994 13.4171 16.9587 13.9577C16.4181 14.4984 16.0241 15.1679 15.814 15.903L15 18.75L14.187 15.904C13.9769 15.1689 13.5829 14.4994 13.0423 13.9587C12.5016 13.4181 11.8321 13.0241 11.097 12.814L8.25 12L11.096 11.187C11.8311 10.9769 12.5006 10.5829 13.0413 10.0423C13.5819 9.50162 13.9759 8.83214 14.186 8.097L14.187 8.096Z">
            </path>
            <path class="path" stroke-linejoin="round" stroke-linecap="round" stroke="black" fill="black"
              d="M6 14.25L5.741 15.285C5.59267 15.8785 5.28579 16.4206 4.85319 16.8532C4.42059 17.2858 3.87853 17.5927 3.285 17.741L2.25 18L3.285 18.259C3.87853 18.4073 4.42059 18.7142 4.85319 19.1468C5.28579 19.5794 5.59267 20.1215 5.741 20.715L6 21.75L6.259 20.715C6.40725 20.1216 6.71398 19.5796 7.14639 19.147C7.5788 18.7144 8.12065 18.4075 8.714 18.259L9.75 18L8.714 17.741C8.12065 17.5925 7.5788 17.2856 7.14639 16.853C6.71398 16.4204 6.40725 15.8784 6.259 15.285L6 14.25Z">
            </path>
            <path class="path" stroke-linejoin="round" stroke-linecap="round" stroke="black" fill="black"
              d="M6.5 4L6.303 4.5915C6.24777 4.75718 6.15472 4.90774 6.03123 5.03123C5.90774 5.15472 5.75718 5.24777 5.5915 5.303L5 5.5L5.5915 5.697C5.75718 5.75223 5.90774 5.84528 6.03123 5.96877C6.15472 6.09226 6.24777 6.24282 6.303 6.4085L6.5 7L6.697 6.4085C6.75223 6.24282 6.84528 6.09226 6.96877 5.96877C7.09226 5.84528 7.24282 5.75223 7.4085 5.697L8 5.5L7.4085 5.303C7.24282 5.24777 7.09226 5.15472 6.96877 5.03123C6.84528 4.90774 6.75223 4.75718 6.697 4.5915L6.5 4Z">
            </path>
            <span class="text_button" @click="getStarted">시작하기</span>
          </button>
          <transition name="fade">
            <div v-if="showArrow" class="down-arrow" @click="smoothScroll">
              <ChevronDown :size="48" />
            </div>
          </transition>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { ChevronDown } from 'lucide-vue-next';
import router from "@/router";
import { mapState, mapActions } from "vuex";
const authenticationModule = "authenticationModule";

export default {
  name: 'FirstContent',
  components: {
    ChevronDown
  },
  props: {
    // videoSource: {
    //   type: String,
    //   required: true
    // },
    overlayTitleOne: {
      type: String,
      default: ''
    },
    overlayTitleTwo: {
      type: String,
      default: ''
    },
    overlayDescription: {
      type: String,
      default: ''
    },
    scrollToY: {
      type: Number,
      default: 0
    },
    scrollDuration: {
      type: Number,
      default: 1000 // 밀리초 단위, 기본값 1초
    }
  },
  setup(props) {
    // const videoPlayer = ref(null);
    const isOverlayVisible = ref(false);
    const showTitle = ref(false);
    const showDescription = ref(false);
    const showButton = ref(false);
    const showArrow = ref(false);

    // const startOverlayTimer = () => {
    //   setTimeout(() => {
    //     showOverlay();
    //   }, 1300);
    // };

    const showOverlay = () => {
      isOverlayVisible.value = true;
      setTimeout(() => {
        showTitle.value = true;
        setTimeout(() => {
          showDescription.value = true;
          setTimeout(() => {
            showButton.value = true;
            setTimeout(() => {
              showArrow.value = true;
            }, 1000);
          }, 1000);
        }, 1000);
      }, 100);
    };

    // const handleError = (event) => {
    //   console.error('Video playback error:', event);
    // };

    const smoothScroll = () => {
      const startPosition = window.pageYOffset;
      const distance = props.scrollToY - startPosition;
      const startTime = performance.now();

      function animation(currentTime) {
        const timeElapsed = currentTime - startTime;
        const run = easeInOutQuad(timeElapsed, startPosition, distance, props.scrollDuration);
        window.scrollTo(0, run);
        if (timeElapsed < props.scrollDuration) {
          requestAnimationFrame(animation);
        }
      }

      function easeInOutQuad(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
      }

      requestAnimationFrame(animation);
    };

    onMounted(() => {
      showOverlay();
    });

    return {
      // videoPlayer,
      isOverlayVisible,
      showTitle,
      showDescription,
      showButton,
      showArrow,
      // startOverlayTimer,
      // handleError,
      smoothScroll,
    };
  },
  computed: {
    ...mapState(authenticationModule, ["isAuthenticated"]),
  },
  methods: {
    getStarted() {
      if (!this.isAuthenticated) {
        // router.push("/login")
        router.push("/user-analysis")  // 로그인하지 않아도 서비스 이용 가능하도록 임시 처리
      }
      else {
        router.push("/user-analysis")
      }
    }
  }
}
</script>

<style scoped>
.main-container {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.background-container {
  display:flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.7);
  background-image: url("@/assets/images/fixed/login/login_background.png");
  background-size: cover;
  background-blend-mode: darken;
}

/* .video-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.fullscreen-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
} */

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /* background-color: rgba(0, 0, 0, 0.5); */ /* 배경색이 있으므로 오버레이 배경은 제거 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 1;
}

.overlay-text {
  text-align: center;
  color: white;
  z-index: 2;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.overlay-text h1 {
  font-size: 3rem;
  opacity: 0;
  transition: opacity 2s ease;
}

.overlay-text h1:last-of-type {
  margin-bottom: 20px;
}

.overlay-text p,
.get-started-btn,
.overlay-text h1 {
  opacity: 0;
  transition: opacity 2s ease;
}

.overlay-text p.fade-in,
.get-started-btn.fade-in,
.overlay-text h1.fade-in, .button.fade-in {
  opacity: 1;
}

.overlay-text p {
  font-size: 1.5rem;
}

.down-arrow {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  color: white;
  animation: bounce 2s infinite;
  cursor: pointer;
}

@keyframes bounce {

  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateY(0) translateX(-50%);
  }

  40% {
    transform: translateY(-10px) translateX(-50%);
  }

  60% {
    transform: translateY(-5px) translateX(-50%);
  }
}

.button {
  --black-700: rgb(31, 31, 31);
  --border_radius: 9999px;
  --transtion: 0.3s ease-in-out;
  --offset: 2px;

  cursor: pointer;
  position: relative;

  display: flex;
  align-items: center;

  transform-origin: center;

  padding: 1rem 2rem;
  background-color: transparent;

  border: none;
  border-radius: var(--border_radius);
  transform: scale(calc(1 + (var(--active, 0) * 0.1)));
  transition: transform var(--transtion);
  opacity: 0;
  transition: opacity 2s ease, transform var(--transtion);
}

.button::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  width: 100%;
  height: 100%;
  background-color: var(--black-700);

  border-radius: var(--border_radius);

  transition: all var(--transtion);
  z-index: 0;
}

.button::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  width: 100%;
  height: 100%;
  background-color: rgba(255, 144, 51, 0.75);
  background-image: radial-gradient(at 51% 89%,
      rgba(255, 144, 51, 1) 0px,
      transparent 50%),
    radial-gradient(at 100% 100%, rgba(255, 144, 51, 1) 0px, transparent 50%),
    radial-gradient(at 22% 91%, rgba(255, 144, 51, 1) 0px, transparent 50%);
  background-position: top;

  opacity: var(--active, 0);
  border-radius: var(--border_radius);
  transition: opacity var(--transtion);
  z-index: 2;
}

.button:is(:hover, :focus-visible) {
  --active: 1;
}

.button:active {
  transform: scale(1);
}

.button .dots_border {
  --size_border: calc(100% + 2px);

  overflow: hidden;

  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  width: var(--size_border);
  height: var(--size_border);
  background-color: transparent;

  border-radius: var(--border_radius);
  z-index: -10;
}

.button .dots_border::before {
  content: "";
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
  transform-origin: left;
  transform: rotate(0deg);

  width: 100%;
  height: 2rem;
  background-color: white;

  mask: linear-gradient(transparent 0%, white 120%);
  animation: rotate 2s linear infinite;
}

@keyframes rotate {
  to {
    transform: rotate(360deg);
  }
}

.button .sparkle {
  position: relative;
  z-index: 10;

  width: 1.75rem;
}

.button .sparkle .path {
  fill: currentColor;
  stroke: currentColor;

  transform-origin: center;

  color: hsl(0, 0%, 100%);
}

.button:is(:hover, :focus) .sparkle .path {
  animation: path 1.5s linear 0.5s infinite;
}

.button .sparkle .path:nth-child(1) {
  --scale_path_1: 1.2;
}

.button .sparkle .path:nth-child(2) {
  --scale_path_2: 1.2;
}

.button .sparkle .path:nth-child(3) {
  --scale_path_3: 1.2;
}

@keyframes path {

  0%,
  34%,
  71%,
  100% {
    transform: scale(1);
  }

  17% {
    transform: scale(var(--scale_path_1, 1));
  }

  49% {
    transform: scale(var(--scale_path_2, 1));
  }

  83% {
    transform: scale(var(--scale_path_3, 1));
  }
}

.button .text_button {
  position: relative;
  z-index: 10;
  color: #ffffff;
  font-size: 1rem;
}

.text_button {
  position: relative;
  z-index: 10;
  color: #ffffff;
  font-size: 1rem;
}

.text_button.fade-in {
  opacity: 1;
}
</style>