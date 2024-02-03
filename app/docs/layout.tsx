"use client";

import Sidebar from "@/components/Sidebar";

export default function MdxLayout({ children }: { children: React.ReactNode }) {
    return (
        <>
            <div className="flex h-dvh max-h-dvh flex-col overflow-hidden">
                <div className="relative flex h-full">
                    <Sidebar />
                    <main className="prose prose-indigo w-full max-w-none overflow-y-auto rounded-xl p-10 prose-h1:bg-gradient-to-br prose-h1:from-indigo-600 prose-h1:to-rose-400 prose-h1:bg-clip-text prose-h1:text-transparent prose-pre:border prose-img:w-full prose-img:rounded-xl">
                        {children}
                    </main>
                </div>
            </div>
        </>
    );
}
