import actions, { AccountActions } from "./actions"


export interface AccountModule {
    namespaced: true
    actions: AccountActions
}

const accountModule: AccountModule = {
    namespaced: true,
    actions,
}

export default accountModule