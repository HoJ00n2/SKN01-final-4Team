import { MutationTree } from "vuex";
import { SurveyState, Survey, Question, Selection } from "./states";
import { REQUEST_LIST_SURVEY_QUESTION_TO_DJANGO, REQUEST_LIST_SURVEY_SELECTION_TO_DJANGO } from "./mutation-types";


export interface SurveyMutations extends MutationTree<SurveyState> {
    [REQUEST_LIST_SURVEY_QUESTION_TO_DJANGO](state: SurveyState, receivedData: Survey): void;
    [REQUEST_LIST_SURVEY_SELECTION_TO_DJANGO](state: SurveyState, selections: Selection[]): void; // 선택지 변이 추가
}

const mutations: MutationTree<SurveyState> = {
    [REQUEST_LIST_SURVEY_QUESTION_TO_DJANGO](state: SurveyState, receivedData: Survey): void {
        state.survey = receivedData; // 설문 저장
        console.log('Mutations에서 받은 데이터: ', receivedData)
        state.questions = receivedData.questions; // 질문 목록 저장
    },
    [REQUEST_LIST_SURVEY_SELECTION_TO_DJANGO](state: SurveyState, selections: Selection[]): void {
        console.log('Mutations에서 받은 선택지: ', selections)
        state.selections = selections; // 선택지 저장
    }
};

export default mutations as SurveyMutations;
