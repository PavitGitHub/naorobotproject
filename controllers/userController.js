var { nao } = require('./dataController');
var credientials = { user: null, expiry: Date.now() };

const setUser = function(req, res)
{
    res.status(200).send('Success');
}

const verifyUser = function(req, res)
{
    if (!credientials.user || Date.now() > credientials.expiry)
    {
        return res.status(403).send('Failed. invalid/expired credientials');
    }
    res.status(200).send('Success');
}

module.exports = { setUser, verifyUser };