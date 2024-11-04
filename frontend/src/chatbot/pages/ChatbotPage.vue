<template>
  <div class="chatbot-container">
    <!-- <video ref="videoPlayer" class="fullscreen-video" :src="videoSource" autoplay muted loop playsinline
          @error="handleError"></video> -->
    <div class="content-overlay">
      <header class="chatbot-header">
        <h1>제공해주신 답변을 기반으로<br>당신의 성향에 대해 분석해봤어요!</h1>
      </header>
      <main class="chatbot-main">
        <message-container ref="messageContainer" :messages="messages"/>
        <send-message
        :messages="messages"
        @send-message="addMessage"/>
      </main>
    </div>
  </div>
</template>

<script>
import { Link } from 'lucide-vue-next';
import SendMessage from './ui/sendMessage.vue';
import MessageContainer from './ui/messageContainer.vue';

export default {
  components: {
    SendMessage,
    MessageContainer
  },
  data() {
    return {
      // videoSource: '/videos/survey-background.mp4',
      // videoPlayer: null,
      messages: [],
      surveyData: null,  // 설문 데이터 저장
      waitingMessage: '성향 분석 중 (15초 정도 소요됩니다)',  // 대기 메시지 기본 값
      waitingDots: 1,    // 점의 개수
      intervalId: null   // setInterval ID
    };
  },
  created() {
    // router에서 설문 데이터 받아오기
      this.surveyData = history.state.surveyData;
      console.log("Received surveyData:", this.surveyData);

      this.sendSurveyToFastAPI();
      this.startWaitingMessage();  // 대기 메시지 애니메이션 시작
  },
  methods: {
    // handleError(event) {
    //   console.error('Video playback error:', event);
    // },
    async sendSurveyToFastAPI() {
      try {
        const waitingMessageIndex = this.messages.push({ text: this.waitingMessage, isUser: false }) - 1;
        const strategy = await this.$store.dispatch('userAnalysisInputModule/sendUserAnalysisToFastAPI', this.surveyData);
        console.log("Strategy:", strategy);
        this.fullResponse = strategy.generatedStrategy;

        this.messages.splice(waitingMessageIndex, 1);
        this.stopWaitingMessage();  // 대기 메시지 애니메이션 종료

        this.messages.push({ text: `📢 당신을 위한 맟춤형 인플루언서 성장 전략을 제공해드릴게요! \n\n${strategy.generatedStrategy}`, isUser: false });
        // this.messages.push({
        //   text: `💬 더 나은 서비스를 제공하기 위해 설문조사에 참여해 주세요! <br> <a href="https://forms.gle/SZbyJAiSTwyoKtz66" target="_blank">구글 폼 설문조사 바로가기</a>`,
        //   isUser: false
        // });
      } catch (error) {
        console.error("FastAPI 요청 오류:", error);
      }
    },
    startWaitingMessage() {
      this.intervalId = setInterval(() => {
        this.waitingDots = (this.waitingDots % 3) + 1;  // 점의 개수를 1, 2, 3 순서로 변경
        this.waitingMessage = `성향 분석 중 (15초 정도 소요됩니다)${'.'.repeat(this.waitingDots)}`;  // 점 개수에 따라 메시지 업데이트

        // 마지막 메시지 업데이트
        if (this.messages.length > 0 && !this.messages[this.messages.length - 1].isUser) {
          this.messages[this.messages.length - 1].text = this.waitingMessage;
        }
      }, 500);  // 0.5초 간격으로 메시지 변경
    },
    stopWaitingMessage() {
      clearInterval(this.intervalId);  // setInterval 중지
      this.intervalId = null;
    },
    scrollToBottom() {
      this.$nextTick(() => {
        const container = this.$refs.messageContainer.$el;
        if (container) {
          container.scrollTop = container.scrollHeight;
        }
      });
    },
    addMessage(message) {
      this.messages.push(message);
      this.scrollToBottom();
    }
  },
  watch: {
    messages: {
      handler() {
        this.scrollToBottom();
      },
      deep: true
    }
  }
}
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

* {
  font-family: 'Noto Sans KR', sans-serif;
}

.chatbot-container {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  display:flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.7);
  background-image: url("@/assets/images/fixed/chatbot/background_gradient.png");
  background-size: cover;
  background-blend-mode: darken;
}

.chatbot-header {
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  margin-top: 60px;
  max-width: 800px;
  width: 100%;
}

.chatbot-main {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  padding: 1rem;
}


/* .fullscreen-video {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
} */

.content-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
  box-sizing: border-box;
  background-color: rgba(255, 255, 255, 0.6);
}

</style>