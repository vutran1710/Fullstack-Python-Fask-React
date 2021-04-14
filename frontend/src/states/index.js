import create from 'zustand'
import { Http } from '../services'


export const state = {
  files: [],
  fileInfo: {},
  dataReport: {},
  activeFile: undefined,
  pendingFile: undefined,
  needCheckFile: undefined,
  checkingStatus: undefined,
}

export const actions = (set, get) => ({
  generateButtonClick: () => Http
    .generateData(10000)
    .json(resp => set({
      pendingFile: resp.file,
      needCheckFile: resp.file,
      fileInfo: {
	...get().fileInfo,
	[resp.file]: {
	  name: resp.file,
	  url: `${Http.serverUrl}/static-data/${resp.file}`
	},
      }
    })),

  checkStatusIntervally: () => {
    const file = get().pendingFile
    set({ checkingStatus: file })
    const check = setInterval(() => {
      Http.checkFileStatus(file).json(resp => {
	if (resp.status === 'FINISH') {
	  set({ checkingStatus: undefined, needCheckFile: undefined })
	  clearInterval(check)
	}
      })
    }, 1000)
  },

  getReportData: () => {
    const file = get().pendingFile
    const files = get().files
    const reports = get().dataReport
    Http.getDataReport(file).json(report => {
      if (!Object.values(report).length) return undefined
      const dataReport = { ...reports, [file]: report }
      set({
	dataReport,
	pendingFile: undefined,
	activeFile: file,
	files: [...files, file],
      })
    })
  },
})

export const useAppStore = create((set, get) => ({
  ...state,
  ...actions(set, get),
}))


// Some helper functions
export const last = array => array[array.length-1]
