<template>
    <button class="google-login-btn" @click="googleLoginClick"></button>
</template>

<script>
import { useStore } from 'vuex'
const googleAuthenticationModule = 'googleAuthenticationModule'

export default {
    setup() {
        const store = useStore()
        const googleLoginClick = async () => {
            console.log("googlelogin클릭")
            await store.dispatch("googleAuthenticationModule/requestGoogleOauthRedirectionToDjango")
        }
        return {
            googleLoginClick
        }
    },
}
</script>

<style scoped>
.google-login-btn {
    margin: 10px 0;
    background-image: url("@/assets/images/fixed/login/google_login_round.png");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    height: 80px;
    width: 80px;
}
</style>