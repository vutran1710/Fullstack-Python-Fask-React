import wretch from 'wretch'

const apiEndpoint = process.env.REACT_APP_API_ENDPOINT
const Request = wretch(apiEndpoint)

const API = {
  generateData: '/gen-data',
  checkStatus: '/check-status',
  dataReport: '/data-report',
}

const abstractRequest = endpoint => (params={}) => Request
      .url(endpoint)
      .query(params)
      .get()

export const generateData = size => abstractRequest(API.generateData)({ size })
export const checkFileStatus = file => abstractRequest(API.checkStatus)({ file })
export const getDataReport = file => abstractRequest(API.dataReport)({ file })
