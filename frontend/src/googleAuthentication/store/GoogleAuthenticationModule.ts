import actions, { googleAuthenticationActions } from "./actions"
export interface GoogleAuthenticationModule {
    namespaced: true
    actions: googleAuthenticationActions
}
const googleAuthenticationModule: GoogleAuthenticationModule = {
    namespaced: true,
    actions,
}
export default googleAuthenticationModule