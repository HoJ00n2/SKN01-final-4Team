<template>
  <div class="main-container">
    <div class="title">
      <h2>쿠잉 서비스 사용 경험 피드백</h2>
      <h4>쿠잉 서비스 사용 경험에 대해 피드백을 남겨주시면<br>더 좋은 서비스를 만드는데에 사용하겠습니다.</h4>
    </div>
    <div class="survey-container">
      <div v-for="(question, index) in questions" :key="index" :ref="`question-${index}`" class="question-box">
        <h2>{{ question.question_text }}</h2>

        <!-- 선택형 질문 -->
        <div v-if="question.survey_type === '4'" class="custom">
          <div v-for="selection in selections" :key="selection.id" class="option">
            <div v-if="selection.question_id === question.id">
              <input
                type="radio"
                :id="`question-${question.id}-${selection.id}`"
                :name="'question-' + question.id"
                :value="selection.custom_text"
                v-model="question.answer"
                @change="answerQuestion(index)"
              />
              <label :for="`question-${question.id}-${selection.id}`" class="option-text">{{ selection.custom_text }}</label>
            </div>
          </div>
        </div>

        <!-- 서술형 질문 -->
        <div v-if="question.survey_type === '1'" class="text-input">
          <textarea
            v-model="question.answer"
            @input="answerQuestion(index)"
            placeholder="여기에 답변을 입력하세요"
            rows="3"
          ></textarea>
        </div>
      </div>
    </div>

    <div class="submit-button-container">
      <button @click="submitSurvey" :disabled="!allQuestionsAnswered" class="submit-button">제출하기</button>
    </div>
  </div>
</template>


<script>
  import { mapActions, mapState } from 'vuex';

  export default {
    name: "SurveyPage",
    data() {
      return {
        surveyId: '1',
        questions: [], // 설문 질문 목록
        selections: []
      };
    },
    computed: {
      ...mapState('surveyModule', ['questions', 'selections']),
      
      allQuestionsAnswered() {
        return this.questions.every(q => q.answered)
      }
    },
    methods: {
      ...mapActions('surveyModule', ['requestListSurveyQuestionToDjango', 'requestListSurveySelectionToDjango', 'requestSubmitSurveyAnswerToDjango']),
      
      async loadSurvey() {
        try {
          // 질문 목록 요청
          const questions = await this.requestListSurveyQuestionToDjango(this.surveyId);
          this.questions = questions;
          console.log(questions);

          let allSelections = []

        // 각 질문에 대해 선택지를 로드하여 selections 배열에 추가
        for (const question of this.questions) {
            console.log(`질문 ID: ${question.id}, survey_type: ${question.survey_type}`);

            if (question.survey_type === "1") {
              console.log(`질문 ID ${question.id}는 서술형 질문입니다. 선택지 없음`)
              continue
            } 

            let options = await this.requestListSurveySelectionToDjango(question.id);

            // 선택지가 배열이 아닌 경우 빈 배열로 초기화
            if (!Array.isArray(options)) {
              options = [];
            }
            console.log('질문당 선택지:', options);
            
            // 선택지가 있는 경우 각 질문에 대한 선택지들을 하나의 리스트로 합침
            allSelections = [...allSelections, ...options]

            console.log(`질문 ID ${question.id}에 대한 선택지 요청 완료`);
        }
        this.selections = allSelections
        console.log('합쳐진 선택지: ', JSON.stringify(this.selections))
        
        } catch (error) {
          console.error('설문조사 로딩 중 오류 발생:', error);
        }
      },
      answerQuestion(index) {
        const question = this.questions[index];
        // 답변 처리(질문이 서술형인지 확인)
        question.answered = question.survey_type === 1 ? question.answer.trim() !== '' : question.answer !== null;
      },
      async submitSurvey() {
        console.log("Survey submitted:", JSON.stringify(this.questions));
        const surveyAnswers = this.questions.map(question => ({
          question_id: question.id,
          answer_data: question.answer || '' // 답변이 없을 경우 빈 문자열로 설정
        }))

        const accountId = null

        try {
            const response = await this.requestSubmitSurveyAnswerToDjango({ survey_answer: surveyAnswers, account_id: accountId })
            console.log('설문이 제출되었습니다:', response)
        } catch (error) {
          console.error('설문 제출 중 오류 발생: ', error)
        }
      }
    },
    created() {
      this.loadSurvey();
    }
  }
</script>

  
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

* {
  font-family: 'Noto Sans KR', sans-serif;
  box-sizing: border-box;
}

.main-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  min-height: 100vh;
}

.title {
  text-align: center;
  margin-bottom: 40px;
}

.title h2 {
  font-size: 28px;
  color: #333;
  margin-bottom: 10px;
}

.title h4 {
  font-size: 16px;
  color: #666;
  font-weight: normal;
  line-height: 1.5;
}

.survey-container {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.question-box {
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 1px solid #eee;
}

.question-box h2 {
  font-size: 18px;
  color: #333;
  margin-bottom: 15px;
}

.customs {
  display: flex;
  flex-direction: column;
}

.option {
  margin-bottom: 10px;
}


.text-input textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  resize: vertical;
}

.submit-button-container {
  text-align: center;
  margin-top: 30px;
}

.submit-button {
  background-color: #6c757d;
  color: white;
  border: none;
  padding: 12px 30px;
  font-size: 16px;
  border-radius: 25px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #ff9033;
}

</style>