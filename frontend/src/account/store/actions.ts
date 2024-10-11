import { ActionContext } from "vuex"
import axiosInst from "@/utility/axiosInstance"

export type AccountActions = {
    requestEmailDuplicationCheckToDjango(context: ActionContext<any, any>, email: string): Promise<boolean>
    requestCreateNewAccountToDjango(context: ActionContext<any, any>, accountInfo: { email: string, nickname: string }): Promise<void>
}

const actions: AccountActions = {
    async requestEmailDuplicationCheckToDjango(context: ActionContext<any, any>, email: string): Promise<boolean> {
        const response = await axiosInst.djangoAxiosInst.post(
            '/account/email-duplication-check', { email })
        return response.data.isDuplicate
    },
    async requestCreateNewAccountToDjango(context: ActionContext<any, any>, accountInfo: { email: string, nickname: string }): Promise<void> {
        try {
            await axiosInst.djangoAxiosInst.post('/account/register', accountInfo)
                .then((res) => {
                    if (res.data) {
                        console.log("회원 가입 완료")
                        return false
                    }
                })
        } catch (error) {
            console.error('신규 계정 생성 실패:', error)
            throw error
        }
    },
}

export default actions