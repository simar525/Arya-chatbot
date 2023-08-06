import Chatbot from "https://cdn.jsdelivr.net/gh/CloozoAI/widget/dist/web.js"
    Chatbot.init({
        chatflowid: "ef2aa3e1-2f31-4c65-84a1-9f68a187747b",
        apiHost: "https://botcongfigs0et4123sdjhjsdg6525267576gh36bh37.up.railway.app",
        theme: {
            button: {
               size: "large",
                backgroundColor: "rgba(0,0,0,1)",
                customIconSrc: "//88b226e3f46c42b4f035d481df5e5723.cdn.bubble.io/f1691161690744x890892727264209500/speech-bubble-with-dots.png",
            },
            chatWindow: {
                welcomeMessage: "Hello",
                poweredByTextColor: "#ffffff",
                botMessage: {
                    backgroundColor: "rgba(255,255,255,1)",
                    textColor: "rgba(0,0,0,1)",
                    showAvatar: true,
                    avatarSrc: "//88b226e3f46c42b4f035d481df5e5723.cdn.bubble.io/f1691161691412x948861938415577200/chatbot.png",
                },
                userMessage: {
                    backgroundColor: "rgba(255,255,255,1)",
                    textColor: "rgba(0,0,0,1)",
                    showAvatar: false,
                    avatarSrc: "",
                },
                textInput: {
                    placeholder: "Type your question",
                    backgroundColor: "#ffffff",
                    textColor: "#303235",
                    sendButtonColor: "#3B81F6",
                }
            }
        },
        chatflowConfig: {
            temperature: "0.61",
            modelName: "gpt-3.5-turbo-16k",
            systemMessagePrompt: "I want you to act as a support assistant that I'm having a conversation with. Your name is ‘Cloozo bot’. You will provide me answers from the given info. If the answer is not included, say exactly ‘Ah, I’m not sure of this. Please send an email to support@cloozo.com and someone from our team will get back to you.’ and stop after that. Refuse to answer any question not about the info. Never break character. If a user types 'hi' or 'hello' or 'hey', your response should always be 'Hello! Nice to meet you. How can I help?'.  Strictly reply in English",
    pineconeEnv: "gcp-west",
    pineconeIndex: "index",
    pineconeApiKey: "e6jfj-fjfjf777mf00",
    openAIApiKey: "sk-83465834653465"
            }
    })