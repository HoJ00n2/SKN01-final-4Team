import { MutationTree } from "vuex";
import { UserAnalysisInputState } from "./states";
import { REQUEST_USER_ANALYSIS_INPUT_TO_FASTAPI } from "./mutation-types";

export interface UserAnalysisInputMutations extends MutationTree<UserAnalysisInputState> {
    [REQUEST_USER_ANALYSIS_INPUT_TO_FASTAPI](state: UserAnalysisInputState, settingValue: string): void
}

const mutations: MutationTree<UserAnalysisInputState> = {
    [REQUEST_USER_ANALYSIS_INPUT_TO_FASTAPI](state: UserAnalysisInputState, settingValue: string): void {
        state.userAnalysisInput = settingValue
    }
}

export default mutations as UserAnalysisInputMutations