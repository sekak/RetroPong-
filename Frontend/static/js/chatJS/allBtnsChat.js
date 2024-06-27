let c = true
let isRequest = false 
let obejctOfChannel = {}
let isListen = false
let web = null

const openSidebar = (sidebar, items) => {
    sidebar.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
    sidebar.style.width = '50%';
    items.forEach(item => {
        item.style.display = 'flex';
    })
    c = false
}

const closeSidebar = (sidebar, items) => {
    sidebar.style.background = '';
    sidebar.style.backgroundColor = 'rgba(0, 0, 0, 0)';
    sidebar.style.width = '80px';
    items.forEach(item => {
        item.style.display = 'none';
    })
    c = true
}

const resetsettings = (sidebar, items) => {
    sidebar.style.background = 'linear-gradient(180deg, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.5) 100%)';
    sidebar.style.width = '80px';
    items.forEach(item => {
        item.style.display = 'flex';
    })
}

function openMenu() {
    const sidebar = document.getElementById('sidebar');
    const items = document.querySelectorAll('.items');

    if (c)
        openSidebar(sidebar, items)
    else if (!c)
        closeSidebar(sidebar, items)
    window.addEventListener('keyup', (e) => {
        if (e.key == 'q')
            closeSidebar(sidebar, items)
    })
    window.addEventListener('resize', () => {
        if (window.innerWidth >= 768)
            resetsettings(sidebar, items)
        else
            closeSidebar(sidebar, items)
    })
}

function appearInfoFriend() {
    const divInfo = document.getElementById('CinfoUser');
    if (divInfo.style.left == '0px')
        divInfo.style.left = '-1000px';
    else
        divInfo.style.left = '0px';
    window.addEventListener('resize', () => divInfo.style.left = '-1000px');
}


function transition(destination) {
    const page_chat = document.getElementById('page_chat'); // page chat
    const page_discover = document.getElementById('page_discover'); // page discover
    const page_discussion = document.getElementById('page_discussion');
    const resUsers = document.getElementById('resUsers');
    const page_channel = document.getElementById('page_channel');

    if (destination == 'chat') {
        page_chat.classList.remove('d-none');
        page_discover.classList.add('d-none');
        page_discussion.classList.add('d-none');
        page_channel.classList.add('d-none');
        filterFriends('online')
    }
    else if (destination == 'discover') {
        page_discover.classList.remove('d-none');
        page_chat.classList.add('d-none');
        page_discussion.classList.add('d-none');
        page_channel.classList.add('d-none');
        filterFriends('online')
    }

}

function changeColor(type) {
    const element = document.getElementById(type);
    const all = document.getElementById('all');
    const online = document.getElementById('online');
    const pending = document.getElementById('pending');
    const blocked = document.getElementById('blocked');
    
    all.classList.remove('text-pink')
    online.classList.remove('text-pink')
    pending.classList.remove('text-pink')
    blocked.classList.remove('text-pink')
    element.classList.add('text-pink')
}


function filterFriends(type) {
    const typeOf = document.getElementById('typeOf');
    const rb_0 = document.querySelectorAll('rb-0');
    const rb_1 = document.getElementById('rb-1');
    const rb_2 = document.getElementById('rb-2');
    const rb_3 = document.getElementById('rb-3');

    if (type == 'online') {
        changeColor('online');
        LoadDataFriend('online')
    }
    else if (type == 'all') {
        changeColor('all');
        LoadDataFriend('all')
    }
    else if (type == 'pending') {
        changeColor('pending');
        LoadDataFriend('pending')
    }
    else if (type == 'blocked') {
        changeColor('blocked');
        LoadDataFriend('blocked')
    }
}


async function sendRequest(target_user_id, target, userId, token) {
    isRequest = true
    const data = await fetchData(`http://127.0.0.1:8002/chat/${target}/${userId}/${target_user_id}`, 'GET', token)
    ws.send(JSON.stringify({"message": "refresh" ,"id": userId , "contact_id": target_user_id,"conversation_id":""}))
    UserContactFetching()
}

async function fetchDataChat(target_user_id)
{ 
    const CcontentConver = document.getElementById('CcontentConver');
    const CinfoUser = document.getElementById('CinfoUser');

    CinfoUser.innerHTML = chatFriendSkeleton(); // skeleton
    CcontentConver.innerHTML = ""
    for(let i = 0; i < 7; i++)
        CcontentConver.innerHTML += contentMessageSkeleton(); // skeleton
    return await DataChatFetching(target_user_id)
}


//socket for channel    
function addSocketChannel() 
{
    const chMessages = document.getElementById('chMessages');
    web = new WebSocket('ws://localhost:8002/ws/chat/channel/')
    web.onopen = ()=>{console.log("connected")}
    web.onmessage = function (event) {
        let data = JSON.parse(event.data)
        chMessages.innerHTML +=  message_channel(data,data)
        chMessages.scrollTop = chMessages.scrollHeight
    }
}

const handleAppearance = (type)=>{
    const page_discussion = document.getElementById('page_discussion');
    const page_chat = document.getElementById('page_chat');
    const page_discover = document.getElementById('page_discover');
    const page_channel = document.getElementById('page_channel');
    const chMessages = document.getElementById('chMessages');
    
    addSocketChannel() // add socket to channel 
    page_chat.classList.add('d-none');
    page_discover.classList.add('d-none');

    for(let i = 0; i < 7; i++)
        chMessages.innerHTML += contentMessageSkeleton(); // skeleton
    if(type === 'toChat')
    {
        page_discussion.classList.remove('d-none');
        page_channel.classList.add('d-none');
    }else if(type === 'toChannel')
    {
        page_discussion.classList.add('d-none');
        page_channel.classList.remove('d-none');
    }
}

// this function is used to fetch channel message
async function fetchMessageChannel(channel_user)
{
    const  {userId, token} = GetUserIdToken();
    const channel_message = await fetchData(`http://127.0.0.1:8002/chat/channel/${channelObj.chID}/other`, 'GET', token)
    obejctOfChannel = {channel_user, channel_message}
    loadDataChannelMessage(channel_message, channel_user)
}

async function implementBtns(target, target_user_id) {
    const Cback = document.getElementById('contact_user');
    const  {userId, token} = GetUserIdToken();
    Cback.src = "/static/img/general/Account.png"

    if (target === 'toChat' && isRequest === false) {
        handleAppearance('toChat') // add socket
        target_id = target_user_id
        const data = await fetchDataChat(target_user_id)
        localStorage.setItem('coversation_id', data.data.conversation_id)
        loadDataChat(data?.data, target_user_id)
    }
    else if (target === 'accept' && isRequest === false)
        sendRequest(target_user_id, "accept", userId, token)
    else if (target === 'decline' && isRequest === false)
        sendRequest(target_user_id, "decline", userId, token)
    else if (target === 'unblock' && isRequest === false)
        sendRequest(target_user_id, "unblock", userId, token)
    //channel
    if(target === 'toChannel')
    {
        handleAppearance('toChannel')
        const channel_user = await fetchData(`http://127.0.0.1:8002/chat/channel/${channelObj.chID}/users`, 'GET', token)
        handleChannelUsers(channel_user)
        fetchMessageChannel(channel_user)
    }
}

function loadDataChannelMessage(channel_message, channel_user){
    const chMessages = document.getElementById('chMessages');
    if(channel_message.status === "200")
    {  
        chMessages.innerHTML = channel_message?.data?.messages?.map(msg => message_channel(msg,channel_user?.data?.users?.find(user=> user.id === msg.cmSender))).join('')
        AddListener() // listener for send message
    }
}

// channel user
function handleChannelUsers(channel_user)
{
    const chUser = document.getElementById('chUser');
    const chTitle = document.getElementById('chTitle');
    const chDesc = document.getElementById('chDesc');

    if(channel_user.status === "200")
    {   
        chTitle.innerHTML = "#" + channelObj?.chName
        chDesc.innerHTML = channelObj?.chDesc
        chUser.innerHTML = channel_user?.data?.users?.map(user => member(user)).join('')
    }
}

// add listener to send message
function AddListener()
{
    const {userId, token} = GetUserIdToken();
    const chsendBtn = document.getElementById('chsendBtn');
    const chInput = document.getElementById('chInput');
    const chMessages = document.getElementById('chMessages');
    
    if(isListen === true)
        return
    chMessages.scrollTop = chMessages.scrollHeight
    chsendBtn.addEventListener('click', () => {
        const value = chInput.value
        if(value === "")
            return
        chInput.value = ""
        chInput.focus()
        web.send(JSON.stringify({"message": value, "id": userId, "channel_id": channelObj.chID,"username":sessionStorage.getItem('username'),"profile": sessionStorage.getItem('profilepic')}))
        isListen = true
    })
}
 