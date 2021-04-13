import create from 'zustand'
import { Http } from '../services'


export const state = {
  fileInfo: [],
  dataReport: {},
  pending_file: undefined,
}

export const actions = (set, get) => ({
  generateButtonClick: () => Http
    .generateData(10000)
    .json(resp => set({ pending_file: resp.file })),

  getReportData: () => {
    const file = get().pending_file
    const reports = get().dataReport
    Http.getDataReport(file).json(report => {
      const dataReport = { ...reports, [file]: report }
      set({ dataReport })
    })
  },
})

export const useAppStore = create((set, get) => ({
  ...state,
  ...actions(set, get),
}))
