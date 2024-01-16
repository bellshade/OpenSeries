import Sidebar from "@/components/Sidebar";

export default async function MdxLayout({ children }: { children: React.ReactNode }) {
    return (
        <>
            <div className="flex h-screen max-h-screen flex-col overflow-hidden">
                <div className="relative flex h-full">
                    <Sidebar />
                    <main className="prose w-full max-w-none overflow-y-auto rounded-xl px-6 py-10 prose-img:rounded-xl">
                        {children}
                    </main>
                </div>
            </div>
        </>
    );
}
