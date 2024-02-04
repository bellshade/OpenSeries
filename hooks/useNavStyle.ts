import { create } from "zustand";

interface NavStyleState {
    isLanding: boolean;
    setDocsStyle: () => void;
    setLandingStyles: () => void;
}

export const useNavStyle = create<NavStyleState>((set) => ({
    isLanding: true,
    setDocsStyle: () => set({ isLanding: false }),
    setLandingStyles: () => set({ isLanding: true })
}));
