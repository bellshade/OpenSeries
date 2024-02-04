"use client";

import { useCallback, useState } from "react";
import { usePython } from "react-py";
import { python } from "@codemirror/lang-python";
import ReactCodeMirror from "@uiw/react-codemirror";
import { vscodeDark } from "@uiw/codemirror-theme-vscode";
import { useTheme } from "next-themes";
import { tomorrow } from "thememirror";

type Props = {
    code: string;
};

const Codeblock = ({ code }: Props) => {
    const [value, setValue] = useState(code);
    const { systemTheme, theme } = useTheme();
    const currentTheme = theme === "system" ? systemTheme : theme;

    const onChange = useCallback((val: string) => {
        setValue(val);
    }, []);

    const { runPython, stdout, stderr, isLoading, isRunning } = usePython();

    return (
        <div className="space-y-4">
            <div className="relative flex max-w-max divide-x divide-indigo-500 overflow-hidden rounded-lg">
                <div
                    className={`absolute inset-0 z-20 grid place-items-center rounded-lg border bg-white dark:border-zinc-700 dark:bg-zinc-900 ${isLoading ? "opacity-100" : "pointer-events-none opacity-0"}`}
                >
                    <span className="icon-[tabler--loader] animate-spin text-2xl"></span>
                </div>
                <button
                    className="grid h-12 w-12 place-items-center bg-indigo-600 font-medium text-white hover:bg-indigo-700"
                    onClick={() => runPython(value)}
                >
                    {isRunning ? (
                        <span className="icon-[ri--loader-3-line] h-6 w-6 animate-spin"></span>
                    ) : (
                        <span className="icon-[iconamoon--player-play] h-6 w-6"></span>
                    )}
                </button>
                <button
                    className="grid h-12 w-12 place-items-center bg-indigo-600 font-medium text-white hover:bg-indigo-700"
                    onClick={() => setValue(code)}
                >
                    <span className="icon-[mdi--restart] h-6 w-6"></span>
                </button>
                <button
                    className="flex items-center gap-2 bg-indigo-600 px-5 py-2.5 font-medium text-white hover:bg-indigo-700"
                    onClick={() => alert("blm cuy")}
                >
                    Buka di Playground
                </button>
            </div>
            <div className="relative overflow-hidden rounded-xl border dark:border-zinc-700">
                <div
                    className={`absolute inset-0 z-20 grid place-items-center bg-white dark:bg-zinc-900 ${isLoading ? "opacity-100" : "pointer-events-none opacity-0"}`}
                >
                    <span className="flex items-center gap-2 text-xl font-bold text-zinc-600 dark:text-zinc-400">
                        <span className="icon-[tabler--loader] animate-spin text-2xl"></span>
                        Loading Environment
                    </span>
                </div>
                <div className="grid divide-x divide-y dark:divide-zinc-700 sm:grid-cols-2">
                    <div>
                        <ReactCodeMirror
                            value={value}
                            theme={currentTheme === "dark" ? vscodeDark : tomorrow}
                            height="400px"
                            extensions={[python()]}
                            onChange={onChange}
                        />
                    </div>
                    <div className="flex p-8">
                        {!stdout && !stderr && !isRunning ? <p>Jalankan kodenya untuk melihat output</p> : null}
                        {stdout}
                        {stderr}
                        {isRunning && <span className="icon-[ri--loader-3-line] m-auto animate-spin text-2xl"></span>}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Codeblock;
