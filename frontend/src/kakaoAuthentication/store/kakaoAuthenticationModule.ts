import actions, { KakaoAuthenticationActions } from "./actions"
export interface KakaoAuthenticationModule {
    namespaced: true
    actions: KakaoAuthenticationActions
}
const kakaoAuthenticationModule: KakaoAuthenticationModule = {
    namespaced: true,
    actions,
}
export default kakaoAuthenticationModule