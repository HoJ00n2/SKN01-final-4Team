import actions, { naverAuthenticationActions } from "./actions"
export interface NaverAuthenticationModule {
    namespaced: true
    actions: naverAuthenticationActions
}
const naverAuthenticationModule: NaverAuthenticationModule = {
    namespaced: true,
    actions,
}
export default naverAuthenticationModule