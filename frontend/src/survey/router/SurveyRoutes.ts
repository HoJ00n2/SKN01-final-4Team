import SurveyPage from "@/survey/pages/SurveyPage.vue"
import SurveyRegisterPage from "@/survey/pages/register/SurveyRegisterPage.vue"

const SurveyRoutes = [
    {
        path: '/survey',
        name: 'SurveyPage',
        component: SurveyPage
    },
    {

        path: '/survey/register',
        name: 'SurveyRegisterPage',
        component: SurveyRegisterPage
    }
]

export default SurveyRoutes
