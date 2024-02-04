"use client";

import { useTheme } from "next-themes";
import { useEffect, useState } from "react";

const ThemeSwitcher = () => {
    const [mounted, setMounted] = useState(false);
    const { systemTheme, theme, setTheme } = useTheme();

    useEffect(() => {
        setMounted(true);
    }, []);

    if (!mounted) {
        return null;
    }

    const renderThemeChanger = () => {
        const currentTheme = theme === "system" ? systemTheme : theme;

        if (currentTheme === "dark") {
            return (
                <button
                    className="grid h-10 w-10 place-items-center rounded-lg text-xl text-yellow-500 hover:bg-zinc-700"
                    onClick={() => setTheme("light")}
                >
                    <span className="icon-[line-md--sun-rising-loop]"></span>
                </button>
            );
        } else {
            return (
                <button
                    className="grid h-10 w-10 place-items-center rounded-lg text-xl text-zinc-600 hover:bg-zinc-200"
                    onClick={() => setTheme("dark")}
                >
                    <span className="icon-[line-md--moon-loop]"></span>
                </button>
            );
        }
    };

    return <>{renderThemeChanger()}</>;
};

export default ThemeSwitcher;
