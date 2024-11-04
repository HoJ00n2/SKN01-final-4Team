import KakaoRedirection from "@/kakaoAuthentication/redirection/KakaoRedirection.vue"
const KakaoAuthenticationRoutes = [
    {
        path: '/kakao_oauth/kakao-access-token',
        name: 'KakaoRedirection',
        component: KakaoRedirection
    },
]
export default KakaoAuthenticationRoutes