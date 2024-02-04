"use client";

import Sidebar from "@/components/Sidebar";
import { useNavStyle } from "@/hooks/useNavStyle";
import { useEffect } from "react";
import { PythonProvider } from "react-py";

export default function MdxLayout({ children }: { children: React.ReactNode }) {
    const { setDocsStyle } = useNavStyle();
    const packages = {
        micropip: ["OpenSeriesBellshade"]
    };

    useEffect(() => {
        setDocsStyle();
    }, [setDocsStyle]);

    return (
        <PythonProvider packages={packages}>
            <Sidebar />
            <main className="prose prose-indigo max-w-none overflow-y-auto rounded-xl p-8 dark:prose-invert prose-pre:border prose-img:w-full prose-img:rounded-xl dark:prose-h1:bg-clip-text dark:prose-h1:font-bold dark:prose-pre:border-zinc-700 lg:pl-80">
                {children}
            </main>
        </PythonProvider>
    );
}
