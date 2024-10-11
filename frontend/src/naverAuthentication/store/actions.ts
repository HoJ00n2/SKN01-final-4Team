import axiosInst from "@/utility/axiosInstance"
import { ActionContext } from "vuex"
import { AxiosResponse } from "axios"

export type naverAuthenticationActions = {
    requestNaverOauthRedirectionToDjango(): Promise<void>
    requestAccessTokenToDjangoRedirection(context: ActionContext<any, any>, payload: { code: string }): Promise<void>
    requestNaverUserInfoToDjango(context: ActionContext<any, any>, payload: { accessToken: string }):Promise<any>
}
const actions: naverAuthenticationActions = {
    async requestNaverOauthRedirectionToDjango(): Promise<void> {
        console.log('requestNaverOauthRedirectionToDjango()')
        return axiosInst.djangoAxiosInst.get('/naver_oauth/naver').then((res) => {
            console.log('url:', res.data.url)
            window.location.href = res.data.url
        })
    },
    async requestAccessTokenToDjangoRedirection(
        context: ActionContext<any, any>,
        payload: { code: string }): Promise<void> {
        try {
            console.log('requestAccessTokenToDjangoRedirection()')
            const { code } = payload
            const response = await axiosInst.djangoAxiosInst.post(
                '/naver_oauth/naver/access-token', { code })
            console.log('accessToken:', response.data.accessToken.access_token)
            return response.data.accessToken.access_token
        } catch (error) {
            console.log('Access Token 요청 중 문제 발생:', error)
            throw error
        }
    },
    async requestNaverUserInfoToDjango(
        context: ActionContext<any, any>,
        payload: { accessToken: string }): Promise<void> {
        try {
            const { accessToken } = payload
            const userInfoResponse: AxiosResponse<any> =
                await axiosInst.djangoAxiosInst.post('/naver_oauth/naver/user-info', { accessToken })
            const userInfo = userInfoResponse.data.user_info
            return userInfo
        } catch (error) {
            alert('사용자 정보 가져오기 실패!')
            throw error
        }
    },
};
export default actions;