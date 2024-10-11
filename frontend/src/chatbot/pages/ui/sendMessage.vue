<template>
    <div class="input-wrapper">
      <input v-model="input"
             @keyup.enter="sendMessage"
             placeholder="메시지를 입력하세요."
             class="message-input" />
      <button @click="sendMessage" class="send-button">
        <i class="mdi mdi-send"></i>
      </button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      messages: {
        type: Array,
        required: true
      },
    },
    data() {
      return {
        input: ''
      };
    },
    methods: {
        sendMessage() {
      if (this.input.trim()) {
        this.$emit('sendMessage', { text: this.input, isUser: true });
        this.input = '';
        setTimeout(() => {
          this.$emit('sendMessage', { text: "안녕하세요! 챗봇은 아직 개발 중이에요. 업데이트 해서 돌아올게요.", isUser: false });
        }, 1000);
      }
    }
    }
  };
  </script>
  
  <style scoped>
  .input-wrapper {
    border-radius: 20px;
  }
  
  .message-input {
    flex-grow: 1;
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 20px;
    background-color: white;
    width: 850px;
    background-color: rgba(255, 255, 255, 0.5);
  }
  
  .send-button {
    margin-left: 10px;
    padding: 0.5rem 1rem;
    background-color: #414141;
    color: white;
    border: none;
    border-radius: 20px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .send-button:hover {
    background-color: #414141;
  }
  
  .message-input:focus + .send-button {
    background-color: #ff9033;
  }
  </style>
  