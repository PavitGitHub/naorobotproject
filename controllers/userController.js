var { nao } = require('./dataController');

const setUser = function(req, res)
{
    res.status(200).send('Success');
}

const verifyUser = function(req, res)
{
    res.status(200).send('Success');
}

module.exports = { setUser, verifyUser };