import actions, { UserAnalysisInputActions } from "./actions"
import mutations, { UserAnalysisInputMutations } from "./mutations"
import state, { UserAnalysisInputState } from "./states"


export interface UserAnalysisInputModule {
    namespaced: true,
    state: UserAnalysisInputState,
    actions: UserAnalysisInputActions,
    mutations: UserAnalysisInputMutations,
}

const userAnalysisInputModule: UserAnalysisInputModule = {
    namespaced: true,
    state,
    actions,
    mutations
}

export default userAnalysisInputModule
