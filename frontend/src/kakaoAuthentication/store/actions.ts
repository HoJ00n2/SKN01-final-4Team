import axiosInst from "@/utility/axiosInstance"
import { AxiosResponse } from "axios"
import { ActionContext } from "vuex"

export type KakaoAuthenticationActions = {
    requestKakaoOauthRedirectionToDjango(): Promise<void>
    requestAccessTokenToDjangoRedirection(
        context: ActionContext<any, any>,
        payload: { code: string }): Promise<void>
    requestKakaoUserInfoToDjango(context: ActionContext<any, any>, payload: { accessToken: string }): Promise<any>
}

const actions: KakaoAuthenticationActions = {
    async requestKakaoOauthRedirectionToDjango(): Promise<void> {
        console.log('requestKakaoOauthRedirectionToDjango()')
        return axiosInst.djangoAxiosInst.get('/kakao_oauth/kakao').then((res) => {
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
                'kakao_oauth/kakao/access-token', { code })
            console.log('accessToken:', response.data.accessToken.access_token)
            return response.data.accessToken.access_token
        } catch (error) {
            console.log('Access Token 요청 중 문제 발생:', error)
            throw error
        }
    },
    async requestKakaoUserInfoToDjango(
        context: ActionContext<any, any>,
        payload: { accessToken: string }): Promise<void> {
        try {
            const { accessToken } = payload
            const userInfoResponse: AxiosResponse<any> =
                await axiosInst.djangoAxiosInst.post(
                    '/kakao_oauth/kakao/user-info',
                    { access_token: accessToken });

            console.log('User Info:', userInfoResponse.data.user_info);
            return userInfoResponse.data.user_info;
        } catch (error) {
            alert('사용자 정보 가져오기 실패!');
            throw error;
        }
    }
};

export default actions;