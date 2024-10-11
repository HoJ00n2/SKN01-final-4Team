export interface SurveyState {
    surveys: Survey[];
    survey: Survey | null;
    selections: Selection[]; // 선택지 배열
    questions: Question[]; // 질문 배열
}

export interface Survey {
    id: number;
    title: string;
    description: string;
    questions: Question[]; // 질문 배열
}

export interface Question {
    id: number;
    question_text: string;
    survey_type: string; // 질문 유형
    answer?: string | null; // 사용자 입력 답변
    answered?: boolean; // 질문이 답변되었는지
    selections?: Selection[]; // 선택지가 있을 경우
}

export interface Selection {
    id: number;
    question_id: number;
    custom_text: string;
    value: string; // 선택지 값 추가
}

export interface SurveyAnswer {
    question_id: number;
    answer_data: string | number | boolean;
}

const state: SurveyState = {
    surveys: [],
    survey: null,
    selections: [],
    questions: []
};

export default state;


