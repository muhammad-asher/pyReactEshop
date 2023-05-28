import {createStore,combineReducers,applyMiddleware} from 'redux'
import thunk from 'redux-thunk'
import {composeWithDevTools} from 'redux-devtools-extension'


const reducer = combineReducers({})

const initalState ={}

const middleWare = thunk

const store = createStore(reducer,initalState,
    composeWithDevTools(applyMiddleware(middleWare)))


export default store