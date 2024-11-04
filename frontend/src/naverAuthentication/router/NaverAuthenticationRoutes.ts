import NaverRedirection  from "../redirection/NaverRedirection.vue"
const NaverAuthenticationRoutes = [
    {
        path: '/naver_oauth/naver-access-token',
        name: 'NaverRedirecton',
        component: NaverRedirection
    },
]
export default NaverAuthenticationRoutes