<template>
    <div class="message-container" ref="messageContainer">
          <div v-for="(message, index) in messages" :key="index" 
               :class="['message-row', message.isUser ? 'user-message' : 'bot-message']">
            <img :src="message.isUser ? require('@/assets/images/fixed/chatbot/user_avatar.png') : require('@/assets/images/fixed/chatbot/cooing_logo.png')"
                 :alt="message.isUser ? 'User avatar' : 'Bot avatar'" 
                 class="message-avatar">
            <div v-if="message.isUser" class="message-bubble">
              {{ message.text }}
            </div>
            <div v-else class="message-bubble" v-html="formatMessage(message.text)">
            </div>
          </div>
        </div>
</template>

<script>
import { marked } from 'marked';
export default {
    props: {
        messages: {
            type: Array,
            required: true
        }
    },
    methods: {
        formatMessage(message) {
            return marked(message);
            // return message.replace(/\n/g, '<br>');
        }
    }
}
</script>

<style>
.message-container {
  flex-grow: 1;
  overflow-y: auto;
  padding: 1rem;
  width: 100%;
  max-width: 800px;
  max-height: 500px;
  margin: 0 auto;
  border-radius: 10px;
  margin-right: 80px;
}

.message-container::-webkit-scrollbar {
  display: none;
}

.message-row {
  display: flex;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.user-message {
  flex-direction: row-reverse;
  align-self: flex-end;
}

.bot-message {
  flex-direction: row;
  align-self: flex-start;
}

.message-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin: 0 10px;
  border: 2px solid transparent;
}

.message-bubble {
  padding: 20px 40px; 
  border-radius: 20px;
  max-width: 70%;
  word-wrap: break-word;
  white-space: pre-wrap;
  line-height: 1.5;
}

.message-bubble h3 {
  margin-left: -10px; /* h3 태그를 왼쪽으로 10px 이동 */
  margin-top: 10px;
}

/* 마크다운 리스트에 스타일 적용 */
.message-bubble ul,
.message-bubble ol {
  padding-left: 20px; /* 리스트 전체를 오른쪽으로 이동 */
  margin-top: -10px;
}

.markdown-content li {
  margin-bottom: 10px;
}

.user-message .message-bubble {
  background-color: #ff9033;
  color: white;
  border-top-right-radius: 0;
}

.bot-message .message-bubble {
  background-color: #f1f1f1;
  color: black;
  border-top-left-radius: 0;
}

</style>