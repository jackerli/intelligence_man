import Vue from 'vue'
import Router from 'vue-router'

import Audio2Text from "@/components/Audio2Text";
import Text2Audio from "@/components/Text2Audio";
import AIReply from "@/components/AIReply";


Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Audio2Text',
            component: Audio2Text
        },
        {
            path: '/text2audio',
            name: 'Text2Audio',
            component: Text2Audio
        },
        {
            path: '/aireply',
            name: 'AIReply',
            component: AIReply
        }
    ]
})