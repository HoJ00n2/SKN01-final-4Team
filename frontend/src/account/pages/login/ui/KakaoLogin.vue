<template>
    <button class="kakao-login-btn" @click="kakaoLoginClick"></button>
</template>

<script>
const kakaoAuthenticationModule = 'kakaoAuthenticationModule'
import { useStore } from "vuex";
export default {
    setup() {
        const store = useStore();
        const kakaoLoginClick = async () => {
            console.log("kakaoLoginClick")
            await store.dispatch(
                "kakaoAuthenticationModule/requestKakaoOauthRedirectionToDjango"
            );

        };
        return {
            kakaoLoginClick,
        };
    },
}
</script>

<style scoped>
.kakao-login-btn {
    margin: 10px 0;
    background-image: url("@/assets/images/fixed/login/kakao_login_round.png");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    height: 80px;
    width: 80px;
}
</style>