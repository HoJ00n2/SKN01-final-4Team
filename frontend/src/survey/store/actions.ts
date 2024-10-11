import { Action, ActionContext } from "vuex"
import { SurveyState, SurveyAnswer } from "./states"
import axios, { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_LIST_SURVEY_QUESTION_TO_DJANGO } from "./mutation-types"

export type SurveyActions = {
    requestCreateSurveyToDjango(context: ActionContext<SurveyState, any>, 
        payload: {title: string, description: string}): Promise<AxiosResponse>,
    requestCreateSurveyQuestionToDjango(
        context: ActionContext<SurveyState, any>, 
        payload: { survey: number, question: string, survey_type: number }
    ): Promise<AxiosResponse>,
    requestCreateSurveySelectionToDjango(
        constext: ActionContext<SurveyState, any>,
        payload: { question_id: number, custom_text: string }
    ): Promise<AxiosResponse>,
    requestListSurveyQuestionToDjango(context: ActionContext<SurveyState,any>,
        surveyId: string
    ): Promise<void>,
    requestListSurveySelectionToDjango(context: ActionContext<SurveyState, any>,
        questionId: string
    ): Promise<void>,
    requestSubmitSurveyAnswerToDjango(context: ActionContext<SurveyState, any>,
        payload: { survey_answer: SurveyAnswer[], account_id: string | null }
    ): Promise<AxiosResponse>
}

const actions: SurveyActions = {
    async requestCreateSurveyToDjango(context: ActionContext<SurveyState, any>, 
        payload: {
            title: string, 
            description: string
        }): Promise<AxiosResponse> {
            const { title, description } = payload
            try {
                const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('/survey/create', payload)
                return res.data
            } catch (error) {
                console.log('requestCreateToDjango() 중 에러 발생')
                throw error
            } 
        },
    async requestCreateSurveyQuestionToDjango(context: ActionContext<SurveyState, any>, 
        payload: {
            survey: number, 
            question: string, 
            survey_type: number 
    }): Promise<AxiosResponse> {
        const { survey, question, survey_type } = payload
        try {
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('survey/create-question', {
                survey,
                question,
                survey_type
            })
            console.log(res.data)
            return res.data
        } catch (error) {
            console.log('requestCreateSurveyQuestionToDjango() 중 에러 발생')
            throw error
        }
    },
    async requestCreateSurveySelectionToDjango(
        constext: ActionContext<SurveyState, any>,
        payload: { question_id: number, custom_text: string }
    ): Promise<AxiosResponse> {
        const { question_id, custom_text } = payload
        try {
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('survey/create-survey-selection', {
                question_id,
                custom_text
            })
            console.log(res.data)
            return res.data
        } catch (error) {
            console.log('requestCreateSurveySelectionToDjango() 중 에러 발생')
            throw error
        }
    },
    async requestListSurveyQuestionToDjango(context: ActionContext<SurveyState,any>,
        surveyId: string
    ): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.djangoAxiosInst.post('survey/list-question',
                { survey_Id: surveyId }
            )
            const data = res.data
            console.log('질문 리스트: ', data)
            return data
        } catch (error) {
            console.error('requestListSurveyQuestionToDjango() 중 에러 발생')
            throw error
        }
    },
    async requestListSurveySelectionToDjango(
        context: ActionContext<SurveyState, any>,
        questionId: string
    ): Promise<void> {
        try {
          const res: AxiosResponse<any, any> = await axiosInst.djangoAxiosInst.post('survey/list-selection', {
            question_Id: questionId 
          });
          
          const data = res.data;
        //   context.commit(REQUEST_LIST_SURVEY_SELECTION_TO_DJANGO, data);
          return data
        } catch (error) {
            console.error('requestListSurveySelectionToDjango() 중 에러 발생')
            throw error
        }
        },
      async requestSubmitSurveyAnswerToDjango(context: ActionContext<SurveyState, any>,
        payload: { survey_answer: SurveyAnswer[], account_id: string | null }
    ): Promise<AxiosResponse> {
        const { survey_answer, account_id } = payload
        try {
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('survey/submit-answer', {
                survey_answer, account_id
            })
            return res.data
        } catch (error) {
            console.log('requestSubmitSurveyAnswerToDjango() 중 에러 발생')
            throw error
        }
    }
}

export default actions;
