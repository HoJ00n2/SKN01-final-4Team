<template>
  <div class="navigation-menu-bar">
    <button @click="goToHomePage" class="logo">COOING</button>
    <div class="center-menu">
      <button class="menu-item button" data-text="피드백" @click="goToSurveyPage">
        <span>피드백</span>
      </button>
      <button class="menu-item button" data-text="성향 분석하기" @click="goToUserAnalysisPage">
        <span >성향 분석하기</span>
      </button>
    </div>
    <div class="auth-buttons">
      <button v-if="!isAuthenticated" @click="goToLoginPage" class="login">
        LOGIN
      </button>
      <button v-if="isAuthenticated" @click="logOut" class="logout">
        LOGOUT
      </button>
    </div>
  </div>
</template>

<script>
import router from "@/router";
import { mapState, mapActions } from "vuex";
const authenticationModule = "authenticationModule";

export default {
  computed: {
    ...mapState(authenticationModule, ["isAuthenticated"]),
  },
  methods: {
    ...mapActions(authenticationModule, [
      "requestLogoutToDjango",
      "checkAndSetAuthStatus"
    ]),
    goToHomePage() {
      router.push("/");
    },
    goToLoginPage() {
      router.push("/login");
    },
    goToSurveyPage() {
      router.push("/survey");
    },
    goToUserAnalysisPage() {
      router.push("/user-analysis");
    },
    async logOut() {
      await this.requestLogoutToDjango();
      this.$router.push("/");
    },
  },
  mounted() {
    console.log("navigation bar mounted()");
    this.checkAndSetAuthStatus();
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

* {
  font-family: 'Noto Sans KR', sans-serif;
}

.navigation-menu-bar {
  position: fixed;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  width: 98%;
  height: 53px;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: rgba(0, 0, 0, 1);
  border-radius: 10px;
  padding: 0 20px;
}

.logo {
  background: none;
  border: none;
  color: rgb(255, 255, 255, 1);
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  padding-bottom: 2px;
}

.center-menu {
  display: flex;
  gap: 20px;
}

.menu-item {
  background: none;
  border: none;
  color: rgb(255, 255, 255, 0.7);
  cursor: pointer;
  font-size: 12px;
  overflow: hidden;
  padding: 0;
  position: relative;
  transition: color 0.3s;
  transition-timing-function: cubic-bezier(0.2, 1, 0.3, 1);
  padding-bottom: 2px;
}

.menu-item::after {
  content: attr(data-text);
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  opacity: 0;
  color: rgb(255, 255, 255, 1);
  transform: translate3d(0, 25%, 0);
}

.menu-item>span {
  display: block;
}

.menu-item::after,
.menu-item>span {
  padding: 0.5em 1em;
  transition: transform 0.6s, opacity 0.6s;
  transition-timing-function: cubic-bezier(0.2, 1, 0.3, 1);
}

.menu-item:hover {
  color: rgb(255, 255, 255, 1);
}

.menu-item:hover::after {
  opacity: 1;
  transform: translate3d(0, 0, 0);
}

.menu-item:hover>span {
  opacity: 0;
  transform: translate3d(0, -25%, 0);
}

.login,
.logout {
  background: none;
  border: none;
  color: rgb(255, 255, 255, 0.7);
  cursor: pointer;
  font-size: 12px;
}

.login:hover{
  color: white;
}

.auth-buttons {
  display: flex;
  align-items: center;
}
</style>