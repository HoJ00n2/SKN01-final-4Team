import actions, { SurveyActions } from "./actions"
import state, { SurveyState } from "./states"
import mutations, { SurveyMutations } from "./mutations"

export interface SurveyModule {
    namespaced: true
    state: SurveyState
    actions: SurveyActions
    mutations: SurveyMutations
}

const surveyModule: SurveyModule = {
    namespaced: true,
    state,
    actions,
    mutations
}

export default surveyModule