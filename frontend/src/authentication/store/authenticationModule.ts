import actions, { AuthenticationActions } from "./actions"
import state, { AuthenticationState } from "./states"
import mutations, { AuthenticationMutations } from "./mutations"


export interface AuthenticationModule {
    namespaced: true
    actions: AuthenticationActions
    state: AuthenticationState
    mutations: AuthenticationMutations
}

const authenticationModule: AuthenticationModule = {
    namespaced: true,
    actions,
    state,
    mutations
}

export default authenticationModule