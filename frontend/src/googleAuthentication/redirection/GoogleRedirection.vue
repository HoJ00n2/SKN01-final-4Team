<template>
  <div></div>
</template>
<script>
import router from '@/router'
import { mapActions } from 'vuex'

const googleAuthenticationModule = 'googleAuthenticationModule'
const accountModule = 'accountModule'
const authenticationModule = 'authenticationModule'

export default {
  data() {
    return {
      accessToken: null,
    }
  },
  methods: {
    ...mapActions(googleAuthenticationModule, ['requestAccessTokenToDjangoRedirection', 'requestGoogleUserInfoToDjango']),
    ...mapActions(accountModule, ['requestEmailDuplicationCheckToDjango', 'requestCreateNewAccountToDjango']),
    ...mapActions(authenticationModule, ['requestAddRedisAccessTokenToDjango']),

    async setRedirectData() {
      const code = this.$route.query.code
      const response = await this.requestAccessTokenToDjangoRedirection({ code })
      if (response) {
        this.accessToken = response;
        this.checkUserExists(this.accessToken)
      }
    },
    async checkUserExists(accessToken) {
      const userInfo = await this.requestGoogleUserInfoToDjango({ accessToken })
      console.log("유저 인포 출력", userInfo)
      if (userInfo.email) {
        const response = await this.requestEmailDuplicationCheckToDjango(userInfo.email)
        if (!response) {
          this.registerNewAccount(userInfo.email, userInfo.name);
          router.push('/survey')
        } else {
          this.registerUserToken(userInfo.email, this.accessToken);
          router.push('/survey')
        }
      }
    },
    async registerNewAccount(email, name) {
      const accountInfo = {
        loginType: 'GOOGLE',
        email: email,
        nickname: name,
      }
      await this.requestCreateNewAccountToDjango(accountInfo)
      this.registerUserToken(email, this.accessToken)
    },
    async registerUserToken(email, accessToken) {
      await this.requestAddRedisAccessTokenToDjango(email, accessToken);
    },
  },
  async created() {
    await this.setRedirectData()
  }
}
</script>