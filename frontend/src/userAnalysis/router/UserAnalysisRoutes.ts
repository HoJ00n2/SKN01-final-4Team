import UserAnalysisPage from "@/userAnalysis/pages/UserAnalysisPage.vue"
import UserAnalysisResultPage from "@/userAnalysis/pages/UserAnalysisResultPage.vue"
const UserAnalysisRoutes = [
    {
        path: '/user-analysis',
        name: 'UserAnalysisPage',
        component: UserAnalysisPage
    },
    {
        path: '/user-analysis/result',
        name: 'UserAnalysisResultPage',
        component: UserAnalysisResultPage
    }
]

export default UserAnalysisRoutes
