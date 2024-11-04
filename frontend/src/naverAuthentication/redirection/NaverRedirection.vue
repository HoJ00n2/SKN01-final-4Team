<template>
    <div></div>
</template>

<script>
import { mapActions } from 'vuex';
const authenticationModule = 'naverAuthenticationModule'
const accountModule = 'accountModule'
const redisModule = 'redisModule'

export default {
    data() {
        return {
            accessToken: null,
        }
    },
    methods: {
        ...mapActions(authenticationModule, [
            'requestAccessTokenToDjangoRedirection', 'requestNaverUserInfoToDjango'
        ]),
        ...mapActions(accountModule, ['requestEmailDuplicationCheckToDjango', 'requestCreateNewAccountToDjango']),
        ...mapActions(redisModule, ['requestAddRedisAccessTokenToDjango']),
        async setRedirectData() {
            const code = this.$route.query.code
            const response = await this.requestAccessTokenToDjangoRedirection({ code })
            if (response) {
                this.accessToken = response;
                this.checkUserExists(this.accessToken)
            }
        },
        async checkUserExists(accessToken) {
            const userInfo = await this.requestNaverUserInfoToDjango({ accessToken })
            if (userInfo.response.email) {
                const response = await this.requestEmailDuplicationCheckToDjango(userInfo.response.email)
                if (!response) {
                    this.registerNewAccount(userInfo.response.email, userInfo.response.nickname)
                } else {
                    this.registerUserToken(userInfo.response.email, this.accessToken)
                }
            }
        },
        async registerNewAccount(email, nickname) {
            const accountInfo = {
                loginType: 'NAVER',
                email: email,
                nickname: nickname,
            }
            await this.requestCreateNewAccountToDjango(accountInfo)
            console.log('전송한 데이터:', accountInfo)
            this.registerUserToken(email, this.accessToken)
        },
        async registerUserToken(email, accessToken) {
            await this.requestAddRedisAccessTokenToDjango(email, accessToken)
        }
    },
    async created() {
        await this.setRedirectData();
    }
}
</script>