<template>
    <div class="survey-form">
      <h2>설문조사 등록</h2>
      <form @submit.prevent="createSurvey">
        <div>
          <label for="title">제목:</label>
          <input id="title" v-model="survey.title" required />
        </div>
        <div>
          <label for="description">설명:</label>
          <textarea id="description" v-model="survey.description" required></textarea>
        </div>
        <v-btn type="submit">설문조사 생성</v-btn>
      </form>
    </div>
  
    <div v-if="surveyId" class="survey-form">
      <form @submit.prevent="addQuestion">
        <div>
          <label for="question">질문:</label>
          <input id="question" v-model="question.questionText" type="text" required />
        </div>
        <div>
          <label for="surveyType">질문 타입:</label>
          <select v-model="question.surveyType" id="surveyType" @change="handleSurveyTypeChange">
            <option :value="1">일반</option>
            <option :value="2">5점</option>
            <option :value="3">불리언</option>
            <option :value="4">사용자 지정</option>
          </select>
        </div>
        <v-btn type="submit">질문 추가</v-btn>
        <!-- 선택지 입력 부분 -->
        <div v-if="questionId && question.surveyType === 4">
          <h3>선택지 추가</h3>
          <div v-for="(custom, index) in customSelections" :key="index">
            <input v-model="customSelections[index]" type="text" placeholder="선택지 입력" />
            <v-btn @click="removeSelection(index)">삭제</v-btn>
          </div>
          <v-btn @click="addSelection">선택지 추가</v-btn>
          <v-btn @click="submitSelections">선택지 등록</v-btn>
        </div> 
      </form>

      <h3>미리보기</h3>
      <div class="preview">
        <h4>{{ survey.title }}</h4>
        <p>{{ survey.description }}</p>
        <h5>질문 목록:</h5>
        <ul>
          <li v-for="(question, index) in questions" :key="index">{{ question.questionText }} (유형: {{ getSurveyTypeLabel(question.surveyType) }})</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import { mapActions } from 'vuex';
  
  const surveyModule = 'surveyModule';
  
  export default {
    data() {
      return {
        survey: {
          title: '',
          description: ''
        },
        surveyId: null,
        question: {
          questionText: '',
          surveyType: 1 // 기본값을 일반으로 설정
        },
        questions: [],
        customSelections: [''], // 선택 항목 배열
        questionId: null,
      };
    },
    methods: {
      ...mapActions(surveyModule, ['requestCreateSurveyToDjango', 'requestCreateSurveyQuestionToDjango', 'requestCreateSurveySelectionToDjango']),
      
      async createSurvey() {
        try {
          const response = await this.requestCreateSurveyToDjango(this.survey);
          this.surveyId = response.title; // 응답에서 받은 id를 surveyId에 저장
          console.log('설문 조사 생성 성공!', this.surveyId);
        } catch (error) {
          console.error('설문 조사 생성 중 에러 발생: ', error);
        }
      },
  
      async addQuestion() {
        if (!this.surveyId) {
          console.error('설문조사가 먼저 생성되어야 합니다.');
          return;
        }
        try {
          const payload = {
            survey: this.surveyId,
            question: this.question.questionText,
            survey_type: this.question.surveyType.toString() // survey_type은 문자열로 전송
          };
          const response = await this.requestCreateSurveyQuestionToDjango(payload);
          this.questionId = response.questionId; // 질문 ID 저장
  
          
  
          // 질문 목록에 추가
          this.questions.push({
            question: this.question.questionText,
            surveyType: this.question.surveyType,
            // options: []
          });
  
          // 사용자 지정 유형이 아닐 경우 폼 초기화
          if (this.question.surveyType !== 4) {
            this.resetQuestionForm();
          }
        } catch (error) {
          console.error('질문 또는 선택지 등록 중 에러 발생: ', error);
        }
      },
  
        async addSelection() {
            this.customSelections.push(''); // 선택 항목 추가
        },
  
      removeSelection(index) {
        this.customSelections.splice(index, 1); // 선택 항목 삭제
      },
  
      handleSurveyTypeChange() {
        if (this.question.surveyType !== 4) {
          this.customSelections = ['']; // 질문 유형이 일반일 경우 선택 항목 초기화
        }
      },
  
      getSurveyTypeLabel(type) {
        const types = {
          1: '서술형',
          2: '5점',
          3: '예/아니요',
          4: '선택형'
        };
        return types[type] || '알 수 없음';
      },
  
      resetQuestionForm() {
        this.question.questionText = ''; // 질문 텍스트 초기화
        this.question.surveyType = 1; // 질문 유형 초기화
        this.customSelections = ['']; // 선택 항목 초기화
        this.questionId = null;
      },
  
      async submitSelections() {
        if (this.customSelections.length > 0) {
          for (const selectionText of this.customSelections) {
            if (selectionText.trim() !== '') {
              const payload = {
                question_id: this.questionId,
                custom_text: selectionText
              };
              try {
                await this.requestCreateSurveySelectionToDjango(payload);
                console.log('선택지 등록 성공:', selectionText);
              } catch (error) {
                console.error('선택지 등록 중 에러 발생: ', error);
              }
            }
          }
          // 선택지 등록 후 현재 질문의 options 업데이트
          const currentQuestion = this.questions.find(q => q.id === this.questionId);
          if (currentQuestion) {
            currentQuestion.options = [...this.customSelections];
          }
          this.resetQuestionForm();
        }
      },
    }
  };
  </script>
  
  <style>
  .survey-form {
    max-width: 600px;
    margin: 100px 200px;
  }
  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  .preview {
    margin-top: 20px;
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 5px;
  }
  </style>
