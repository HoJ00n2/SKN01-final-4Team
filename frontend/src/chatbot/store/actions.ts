import { ActionContext } from "vuex";
import { AxiosResponse } from "axios";
import axiosInst from "@/utility/axiosInstance";
import { UserInputState } from "./states";

export type UserInputActions = {
    sendSurveyToFastAPI(
        context: ActionContext<UserInputState, any>,
        payload: {
            gender: string,
            age_group: string,
            mbti: string,
            topic: string,
            strength: string,
            reveal: string,
            platform: string,
            interested_influencer: string
        }): Promise<any>
}

const actions: UserInputActions = {
    async sendSurveyToFastAPI(
        context: ActionContext<UserInputState, any>,
        payload: {
            gender: string,
            age_group: string,
            mbti: string,
            topic: string,
            strength: string,
            reveal: string,
            platform: string,
            interested_influencer: string
        }): Promise<any> {
        try {
            console.log('sendSurveyToFastAPI()');
            
            // Payload 구조에 맞게 데이터를 준비
            const response = await axiosInst.fastapiAxiosInst.post(
                '/growth-strategy', {
                    gender: payload.gender,
                    age_group: payload.age_group,
                    mbti: payload.mbti,
                    topic: payload.topic,
                    strength: payload.strength,
                    reveal: payload.reveal,
                    platform: payload.platform,
                    interested_influencer: payload.interested_influencer
                }
            );
            
            return response.data;
        } catch (error) {
            console.log('sendSurveyToFastAPI() 중 문제 발생:', error);
            throw error;
        }
    },
}

export default actions;
