const secret = new fernet.Secret("cw_0x689RpI-jtRR7oE8h_eQsKImvJapLeSbXpwF4e4=");
let display = "";
const token = new fernet.Token({
  secret: secret,
  time: Date.parse(1),
  iv: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
})

const generateHash = (e) =>{
    //form handling has issue
    e.preventDefault()
    const value = e.target.value
    hashed_id = token.encode(value)
    request = {
        name : 'some name',
        hash_id : hashed_id 
    }

    response = sendDataToServer(request)
    //display data after mapping the response
}

const sendDataToServer = async (data) =>{
    const endpoint = 'http://localhost:8000/decrypt'
    const serverResponse = await (await fetch(endpoint,{
        method: 'post',
        body: JSON.stringify(data)
    })).json()
    console.log(serverResponse) 
    return serverResponse;
}