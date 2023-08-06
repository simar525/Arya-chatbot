import Chatbot from "https://cdn.jsdelivr.net/gh/CloozoAI/widget/dist/web.js"
    Chatbot.init({
        chatflowid: "47e84926-9025-44b8-b76a-275deed66a91",
        apiHost: "https://botcongfigs0et4123sdjhjsdg6525267576gh36bh37.up.railway.app",
        theme: {
            button: {
               size: "large",
                backgroundColor: "rgba(0,0,0,1)",
                customIconSrc: "//88b226e3f46c42b4f035d481df5e5723.cdn.bubble.io/f1691229901539x554024500723669060/speech-bubble-with-dots.png",
            },
            chatWindow: {
                welcomeMessage: "rgrtg",
                poweredByTextColor: "#ffffff",
                botMessage: {
                    backgroundColor: "rgba(255,255,255,1)",
                    textColor: "rgba(0,0,0,1)",
                    showAvatar: true,
                    avatarSrc: "//88b226e3f46c42b4f035d481df5e5723.cdn.bubble.io/f1691229902683x223887610667643740/chatbot.png",
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
            temperature: "0",
            modelName: "gpt-3.5-turbo",
            systemMessagePrompt: " mjbjkbdfvfdxv If a user types 'hi' or 'hello' or 'hey', your response should always be 'Hello! Nice to meet you. How can I help?'.  Strictly reply in English",
    pineconeEnv: "",
    pineconeIndex: "",
    pineconeApiKey: "",
    openAIApiKey: "wdwqd"
            }
    })