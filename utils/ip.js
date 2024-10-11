const os = require('os');

function getIPAddress() {
    const interfaces = os.networkInterfaces();
    for (let iface in interfaces) {
        for (let i = 0; i < interfaces[iface].length; i++) {
            const address = interfaces[iface][i];
            if (address.family === 'IPv4' && !address.internal) {
                return address.address;
            }
        }
    }
    return 'IP not found';
}

module.exports = {getIPAddress};
